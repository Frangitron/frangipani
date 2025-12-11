from abc import ABC, abstractmethod
import time


class ITimeProvider(ABC):

    @abstractmethod
    def now(self) -> float:
        pass


class TimeProvider(ITimeProvider):

    def now(self) -> float:
        return time.time()
