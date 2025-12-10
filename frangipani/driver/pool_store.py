from abc import ABC, abstractmethod

from frangipani.driver.driver import Driver
from frangipani.driver.pool import DriverPool


class IDriverPoolStore(ABC):
    def __init__(self):
        self._pool: DriverPool = DriverPool(name="Internal")

    @abstractmethod
    def load(self, identifier: str) -> None:
        pass

    @abstractmethod
    def save(self, identifier: str) -> None:
        pass

    @property
    def drivers(self) -> list[Driver]:
        return self._pool.drivers

    def set_pool(self, pool: DriverPool) -> None:
        self._pool = pool
