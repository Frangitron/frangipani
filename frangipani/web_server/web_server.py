import sys
import time
from multiprocessing import Process, Event

from frangipani_web_server.configuration import WebServerConfiguration
from frangipani_web_server.control.definition import WebControlDefinition
from frangipani_web_server.control.type_enum import ControlTypeEnum

from frangipani.web_server.process_wrapper import main_loop
from frangipani.web_server.shared_memory_manager import SharedMemoryManager


class WebServer:
    def __init__(self, configuration: WebServerConfiguration):
        self._configuration = configuration

        self._process: Process | None = None
        self._stop_event = Event()
        self._shared_memory_manager = SharedMemoryManager(
            control_definitions=configuration.control_definitions
        )
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

    def get_value(self, control_address: str) -> float | bool:
        return self._shared_memory_manager.get_value(control_address)

    def get_all_values(self) -> dict[str, float | bool]:
        return self._shared_memory_manager.get_all_values()


if __name__ == "__main__":
    configuration = WebServerConfiguration(
        public_folder=sys.argv[1],
        control_definitions=[
            WebControlDefinition(
                address="/fader1",
                type=ControlTypeEnum.Fader,
                label="Fader 1",
                column=0,
                row=0,
                value=0.0,
                min=0.0,
                max=1.0
            )
        ]
    )

    web_server = WebServer(configuration)
    web_server.start()

    while True:
        try:
            print(web_server.get_all_values())
            time.sleep(1.0 / 10.0)
        except KeyboardInterrupt:
            break

    web_server.stop()
