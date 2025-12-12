from pythonhelpers.injector import Injector

from frangipani.driver.pool_store import IDriverPoolStore

from frangipani.components.components import Components


class DriverUpdater:
    def __init__(self):
        self._driver_pool_store = Injector().inject(IDriverPoolStore)
        self._web_server = Components().web_server

    def read_sources(self) -> None:
        all_values = self._web_server.get_all_values()

        for control, value in all_values.items():
            all_values[control] = tuple(min(max(0.0, float(item)), 1.0) for item in value)

        for driver in self._driver_pool_store.drivers:
            source_identifier  = driver.info.source_identifier
            try:
                driver.set_source_value(all_values[source_identifier.control_address])
            except KeyError:
                raise ValueError(f"No source '{source_identifier.control_address}' found for driver {driver.info.name}") from None
