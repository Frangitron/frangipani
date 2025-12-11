import logging
import sys
import time

from frangipani.web_server import (
    Button,
    ColorWheel,
    ControlOrientationEnum,
    Fader,
    Group,
    Placement,
    Radio,
    WebServer,
    WebServerConfiguration,
    WebServerConfigurationStore,
)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    _logger = logging.getLogger("Script:MakeDemoWebServer")

    configuration = WebServerConfiguration(
        public_folder=sys.argv[1],
        root_control_definition=Group(
            label="Root Control",
            placement=Placement(column=0, row=0),
            controls=[
                Fader(
                    address="dimmer_fixtures_all_parameters",
                    label="DimFix all params",
                    placement=Placement(column=0, row=0),
                    orientation=ControlOrientationEnum.Vertical,
                    value=0.0
                ),
                Fader(
                    address="master_dimmer",
                    label="Master Dimmer",
                    placement=Placement(column=1, row=0),
                    orientation=ControlOrientationEnum.Vertical,
                    value=0.0
                ),
            ]
        )
    )

    web_server_configuration_store = WebServerConfigurationStore()
    web_server_configuration_store.set_configuration(configuration)
    web_server_configuration_store.save("demo.webserver.json")
    web_server = WebServer(configuration=web_server_configuration_store.configuration)
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
