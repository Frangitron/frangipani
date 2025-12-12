from frangipani.driver.driver import Driver
from frangipani.driver.driver_info import DriverInfo
from frangipani.driver.pool_storable import DriverPoolStorable


class DriverPool:
    def __init__(self, name: str, driver_infos: list[DriverInfo] | None = None):
        self.name = name
        self.drivers: list[Driver] = []

        names = set()
        for driver_info in driver_infos or []:
            if driver_info.name in names:
                raise ValueError(f"Duplicate driver name {driver_info.name}")

            names.add(driver_info.name)

            new_driver = Driver(driver_info)
            self.drivers.append(new_driver)

    @staticmethod
    def from_storable(storable: DriverPoolStorable) -> "DriverPool":
        return DriverPool(
            name=storable.name,
            driver_infos=storable.driver_infos
        )

    def to_storable(self) -> DriverPoolStorable:
        return DriverPoolStorable(
            name=self.name,
            driver_infos=[driver.info for driver in self.drivers]
        )
