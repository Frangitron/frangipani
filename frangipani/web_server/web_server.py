from multiprocessing import Process, Event

from frangipani_web_server.configuration import WebServerConfiguration

from frangipani.web_server.process_wrapper import main_loop
from frangipani.web_server.shared_memory_manager import SharedMemoryManager


class WebServer:
    def __init__(self, configuration: WebServerConfiguration):
        self._configuration = configuration

        self._process: Process | None = None
        self._stop_event = Event()
        self._shared_memory_manager = SharedMemoryManager(configuration.root_control_definition)
        self._shared_memory_name = self._shared_memory_manager.create_from_controls()

    def start(self):
        if self._process is not None:
            raise RuntimeError("WebServer already started")

        self._stop_event.clear()
        self._process = Process(
            target=main_loop,
            args=(
                self._configuration,
                self._shared_memory_name,
                self._stop_event
            )
        )
        self._process.start()

    def stop(self):
        self._stop_event.set()
        self._process.join()
        self._process = None
        self._shared_memory_manager.cleanup()

    def get_all_values(self) -> dict[str, tuple[float, ...]]:
        return self._shared_memory_manager.get_all_values()
