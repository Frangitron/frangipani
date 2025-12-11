from pythonhelpers.injector import Injector

from frangipani.time_provider import ITimeProvider


class Interpolator:
    def __init__(self, fade_in_time: float = 0.0, fade_out_time: float = 0.0):
        self._fade_in_time = fade_in_time
        self._fade_out_time = fade_out_time

        self._time_provider = Injector().inject(ITimeProvider)

        self._current_value = 0.0
        self._target = 0.0

        self._last_update_time = -1.0

    def set_target(self, value: float):
        self._target = value

    @property
    def value(self) -> float:
        current_time = self._time_provider.current_time

        if self._last_update_time == current_time:
            return self._current_value
        self._last_update_time = current_time

        duration = self._fade_out_time if self._target == 0.0 else self._fade_in_time

        if duration <= 0.0:
            self._current_value = self._target
            return self._current_value

        step = self._time_provider.delta_time / duration

        if self._current_value < self._target:
            self._current_value = min(self._target, self._current_value + step)
        elif self._current_value > self._target:
            self._current_value = max(self._target, self._current_value - step)

        return self._current_value
