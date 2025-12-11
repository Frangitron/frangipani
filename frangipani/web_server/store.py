from copy import copy

from frangipani_web_server.configuration import WebServerConfiguration


# TODO: use interface and Injector ?
class WebServerConfigurationStore:

    def __init__(self):
        self._configuration: WebServerConfiguration | None = None

    def load(self, identifier: str) -> None:
        with open(identifier, 'r') as file:
            self._configuration = WebServerConfiguration.from_json(file.read())

    def save(self, identifier: str) -> None:
        storable_configuration = copy(self._configuration)
        storable_configuration.message_callback = None
        with open(identifier, 'w') as file:
            file.write(storable_configuration.to_json(indent=2))

    def set_configuration(self, configuration: WebServerConfiguration) -> None:
        self._configuration = configuration

    @property
    def configuration(self) -> WebServerConfiguration:
        return self._configuration
