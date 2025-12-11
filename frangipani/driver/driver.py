from frangipani.driver.driver_info import DriverInfo
from frangipani.math.interpolator import Interpolator


## FIXME very crude implementation (not really working)

class Driver:
    def __init__(self, info: DriverInfo):
        self.info = info
        self._source_value: float = 0.0
        self._previous_value: float = 0.0
        self._interpolator = Interpolator(
            fade_in_time=self.info.fade_in_time,
            fade_out_time=self.info.fade_out_time
        )

    @property
    def value(self) -> float:
        interpolated = self._interpolator.value
        return 1.0 - interpolated if self.info.inverted else interpolated

    def set_source_value(self, value: float | bool | None) -> None:
        if value is not None:
            self._source_value = min(max(0.0, float(value)), 1.0)

        if self._previous_value != self._source_value:
            self._previous_value = self._source_value
            self._interpolator.set_target(self._source_value)

    def __repr__(self):
        return f"<{self.__class__.__name__}(info={self.info})>"
