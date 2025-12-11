from pythonhelpers.injector import Injector

from frangipani.driver.pool_store import IDriverPoolStore

from frangipani.components.components import Components


class DriverUpdater:

    def __init__(self):
        self._driver_pool_store = Injector().inject(IDriverPoolStore)
        self._web_server = Components().web_server

    def read_sources(self) -> None:
        all_values = self._web_server.get_all_values()

        for driver in self._driver_pool_store.drivers:
            source_identifier  = driver.source
            print(driver.name, all_values[source_identifier.control_address])
