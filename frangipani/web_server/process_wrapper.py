from multiprocessing.shared_memory import SharedMemory
from multiprocessing.synchronize import Event as EventType
import atexit
import logging
import signal
import struct
import sys
import time

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


def _signal_handler(sig, frame):
    """
    Handle signals (e.g., SIGINT, SIGTERM) to exit gracefully.
    """
    _logger.info(f"\nReceived signal {sig}, exiting...")
    sys.exit(0)


def _make_callback(shared_memory: SharedMemory, control_map: dict):
    def callback(message: BaseMessage):
        if isinstance(message, UpdateMessage):
            if message.address in control_map:
                offset, fmt = control_map[message.address]
                try:
                    struct.pack_into(fmt, shared_memory.buf, offset, message.value)
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

        atexit.register(lambda: _cleanup(shared_memory))

        signal.signal(signal.SIGINT, _signal_handler)  # Ctrl+C
        signal.signal(signal.SIGTERM, _signal_handler)  # Termination signal

        configuration.message_callback = _make_callback(shared_memory, control_map)

        web_server = FrangipaniWebServer(configuration)
        web_server.start()

        while not stop_event.is_set():
            time.sleep(0.1)

    except KeyboardInterrupt:
        _logger.info("\nKeyboard interrupt received, exiting...")
    finally:
        _cleanup(shared_memory)
        _logger.info("Exiting")
