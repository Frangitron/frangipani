from multiprocessing.shared_memory import SharedMemory
from multiprocessing.synchronize import Event as EventType
import atexit
import logging
import signal
import sys
import time

from frangipani_web_server.configuration import WebServerConfiguration
from frangipani_web_server.control.definition import WebControlDefinition
from frangipani_web_server.server import FrangipaniWebServer

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


def main_loop(configuration: WebServerConfiguration, shared_memory_name: str, stop_event: EventType):
    _logger.info("Starting web server loop...")
    shared_memory = None

    try:
        shared_memory = SharedMemory(name=shared_memory_name)

        atexit.register(lambda: _cleanup(shared_memory))

        signal.signal(signal.SIGINT, _signal_handler)  # Ctrl+C
        signal.signal(signal.SIGTERM, _signal_handler)  # Termination signal

        web_server = FrangipaniWebServer(configuration)

        while not stop_event.is_set():
            time.sleep(1)

    except KeyboardInterrupt:
        _logger.info("\nKeyboard interrupt received, exiting...")
    except Exception as e:
        _logger.info(f"Error: {e}")
    finally:
        _cleanup(shared_memory)
        _logger.info("Exiting")
