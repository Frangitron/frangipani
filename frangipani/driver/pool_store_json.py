from frangipani.driver import Driver
from frangipani.driver.pool import DriverPool
from frangipani.driver.pool_store import IDriverPoolStore


class JsonDriverPoolStore(IDriverPoolStore):

    def load(self, identifier: str) -> None:
        with open(identifier, 'r') as file:
            self._pool = DriverPool.from_json(file.read())

    def save(self, identifier: str) -> None:
        with open(identifier, 'w') as file:
            file.write(self._pool.to_json(indent=2))

    # TODO : domain + abstract ? are we sure ?
    def get_by_name(self, name: str) -> Driver | None:
        for driver in self._pool.drivers:
            if driver.name == name:
                return driver

        return None
