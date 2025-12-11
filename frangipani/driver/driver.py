from pythonhelpers.injector import Injector

from frangipani.driver.driver_info import DriverInfo
from frangipani.time_provider.time_provider import ITimeProvider


## FIXME very crude implementation (not really working)

class Driver:
    def __init__(self, info: DriverInfo):
        self.info = info
        self._source_value: float | bool | None = None
        self._previous_value: float | bool | None = None
        self._latest_change_time: float = 0.0
        self._time_provider = Injector().inject(ITimeProvider)

    @property
    def value(self) -> float | bool | None:
        elapsed_time = self._time_provider.now() - self._latest_change_time

        if self.info.fade_in_time > 0.0 and self._source_value > 0.0 and elapsed_time < self.info.fade_in_time:
            return self._source_value * elapsed_time / self.info.fade_in_time

        if self.info.fade_out_time > 0.0 and self._source_value < 1.0 and elapsed_time < self.info.fade_out_time:
            return 1.0 - elapsed_time / self.info.fade_out_time

        return self._source_value

    def set_source_value(self, value: float | bool | None) -> None:
        if value is not None:
            value = float(value)

        if self._previous_value == value:
            return
        self._previous_value = value

        if self.info.inverted:
            self._source_value = 1.0 - value
        else:
            self._source_value = value

        print(f"Changed source value of {self.info.name} to {self._source_value}")
        self._latest_change_time = self._time_provider.now()

    def __repr__(self):
        return f"<{self.__class__.__name__}(info={self.info})>"
