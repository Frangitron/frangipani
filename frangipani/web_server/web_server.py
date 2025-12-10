import sys
import time
from multiprocessing import Process, Event

from frangipani_web_server.configuration import WebServerConfiguration
from frangipani_web_server.control import Group, Fader, ControlOrientationEnum, Radio, ColorWheel, Button
from frangipani_web_server.control.base.placement import Placement

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

    def get_value(self, control_address: str) -> float | bool:
        return self._shared_memory_manager.get_value(control_address)

    def get_all_values(self) -> dict[str, float | bool]:
        return self._shared_memory_manager.get_all_values()


if __name__ == "__main__":
    configuration = WebServerConfiguration(
        public_folder=sys.argv[1],
        root_control_definition=Group(
            label="Root Control",
            placement=Placement(column=0, row=0),
            controls=[
                Group(
                    label="Faders",
                    placement=Placement(column=0, row=1, spanColumn=4),
                    controls=[
                        Fader(
                            address="/fader1",
                            label="Fader 1",
                            placement=Placement(column=0, row=0),
                            orientation=ControlOrientationEnum.Vertical,
                            value=0.0
                        ),
                        Fader(
                            address="/fader2",
                            label="Fader 2",
                            placement=Placement(column=1, row=0),
                            orientation=ControlOrientationEnum.Vertical,
                            value=0.0
                        ),
                        Fader(
                            address="/fader3",
                            label="Fader 3",
                            placement=Placement(column=2, row=0),
                            orientation=ControlOrientationEnum.Vertical,
                            value=0.5,
                        ),
                        Fader(
                            address="/fader4",
                            label="Fader 4",
                            placement=Placement(column=3, row=0),
                            orientation=ControlOrientationEnum.Vertical,
                            value=0.5,
                        ),
                        Fader(
                            address="/fader5",
                            label="Fader 5",
                            placement=Placement(column=4, row=0),
                            orientation=ControlOrientationEnum.Vertical,
                            value=0.5,
                        ),
                        Radio(
                            address="/radio1",
                            label="Radio 1",
                            placement=Placement(column=0, row=1, spanColumn=4),
                            options=["Option 1", "Option 2", "Option 3", "Option 4"],
                            value=0,
                        ),
                        Radio(
                            address="/radio2",
                            label="Radio 1",
                            placement=Placement(column=0, row=2, spanColumn=4),
                            options=["Option 1", "Option 2"],
                            value=0,
                        ),
                    ]
                ),
                ColorWheel(
                    address="/color_wheel",
                    label="Color Wheel",
                    placement=Placement(column=0, row=2),
                    value=(0.0, 0.0)
                ),
                Button(
                    address="/button1",
                    label="Button 1",
                    placement=Placement(column=1, row=2),
                    value=False
                ),
                Button(
                    address="/button2",
                    label="Button 2",
                    placement=Placement(column=2, row=2),
                    is_toggle=True,
                    value=True
                ),
                Button(
                    address="/button3",
                    label="Button 3",
                    placement=Placement(column=3, row=2),
                    is_toggle=True,
                    value=False
                )
            ]
        )
    )

    web_server = WebServer(configuration)
    web_server.start()

    while True:
        try:
            values = web_server.get_all_values()
            if values:
                print(values)

            time.sleep(1.0 / 10.0)
        except KeyboardInterrupt:
            break

    web_server.stop()
