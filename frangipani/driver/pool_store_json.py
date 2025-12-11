from frangipani.driver.driver import Driver
from frangipani.driver.pool import DriverPool
from frangipani.driver.pool_storable import DriverPoolStorable
from frangipani.driver.pool_store import IDriverPoolStore


class JsonDriverPoolStore(IDriverPoolStore):

    def load(self, identifier: str) -> None:
        with open(identifier, 'r') as file:
            pool = DriverPoolStorable.from_json(file.read())
            self._pool = DriverPool.from_storable(pool)

    def save(self, identifier: str) -> None:
        with open(identifier, 'w') as file:
            file.write(self._pool.to_storable().to_json(indent=2))

    # TODO : domain + abstract ? are we sure ?
    def get_by_name(self, name: str) -> Driver | None:
        for driver in self._pool.drivers:
            if driver.info.name == name:
                return driver

        return None
