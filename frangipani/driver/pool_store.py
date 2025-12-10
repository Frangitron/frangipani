from abc import ABC, abstractmethod

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

    def set_pool(self, pool: DriverPool) -> None:
        self._pool = pool
