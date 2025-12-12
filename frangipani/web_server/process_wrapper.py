from multiprocessing.shared_memory import SharedMemory
from multiprocessing.synchronize import Event as EventType
import asyncio
import atexit
import logging
import signal
import struct

from frangipani_web_server.configuration import WebServerConfiguration
from frangipani_web_server.message.base import BaseMessage
from frangipani_web_server.message.update import UpdateMessage
from frangipani_web_server.server.server import FrangipaniWebServer

from frangipani.web_server.shared_memory_manager import SharedMemoryManager

_logger = logging.getLogger("WebProcessWrapper")


def _cleanup(shared_memory):
    """Clean up resources properly"""
    if shared_memory is not None:
        shared_memory.close()
    _logger.info("Resources cleaned up")


def _make_callback(shared_memory: SharedMemory, control_map: dict):
    def callback(message: BaseMessage):
        if isinstance(message, UpdateMessage):
            if message.address in control_map:
                offset, fmt, factor = control_map[message.address]
                try:
                    if isinstance(message.value, (tuple, list)):
                        struct.pack_into(fmt, shared_memory.buf, offset, *[c * f for c, f in zip(message.value, factor)])
                    else:
                        struct.pack_into(fmt, shared_memory.buf, offset, message.value * factor[0])
                except Exception as e:
                    _logger.error(f"Failed to update shared memory for {message.address}: {e}")

    return callback


def main_loop(configuration: WebServerConfiguration, shared_memory_name: str, stop_event: EventType):
    logging.basicConfig(level=logging.INFO)
    _logger.info("Starting web server loop...")
    shared_memory = None

    try:
        shared_memory = SharedMemory(name=shared_memory_name)

        manager = SharedMemoryManager(configuration.root_control_definition)
        control_map = manager.control_map

        configuration.message_callback = _make_callback(shared_memory, control_map)
        web_server = FrangipaniWebServer(configuration)

        atexit.register(lambda: _cleanup(shared_memory))

        # Run the async loop
        async def run_server():
            await web_server.start_async()

            # Wait until the stop event is set
            while not stop_event.is_set():
                await asyncio.sleep(0.1)

            await web_server.stop_async()

        # Handle signals by setting the event (which breaks the loop above)
        def signal_handler(signum, frame):
            _logger.info(f"Received signal {signum}, stopping...")
            stop_event.set()

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)

        asyncio.run(run_server())

    except KeyboardInterrupt:
        _logger.info("\nKeyboard interrupt received, exiting...")
    finally:
        _cleanup(shared_memory)
        _logger.info("Exiting")
