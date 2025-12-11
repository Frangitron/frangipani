from abc import ABC, abstractmethod
import time


class ITimeProvider(ABC):

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def tick(self) -> None:
        pass

    @property
    @abstractmethod
    def delta_time(self) -> float:
        pass

    @property
    @abstractmethod
    def current_time(self) -> float:
        pass


class TimeProvider(ITimeProvider):

    def __init__(self):
        self._delta_time = 0.0
        self._previous_tick_time = 0.0
        self._current_time = 0.0

        self.reset()

    def reset(self):
        now = time.time()
        self._delta_time = 0.0
        self._previous_tick_time = now
        self._current_time = now

    def tick(self) -> None:
        self._current_time =  time.time()
        self._delta_time = self._current_time - self._previous_tick_time
        self._previous_tick_time = self._current_time

    @property
    def delta_time(self) -> float:
        return self._delta_time

    @property
    def current_time(self) -> float:
        return self._current_time
