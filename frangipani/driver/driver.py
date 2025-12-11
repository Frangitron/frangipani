from frangipani.driver.driver_info import DriverInfo


class Driver:
    def __init__(self, info: DriverInfo):
        self.info = info
        self._source_value: float | bool | None = None

    @property
    def value(self) -> float | bool | None:
        return self._source_value

    def set_source_value(self, value: float | bool | None) -> None:
        if self.info.inverted:
            self._source_value = 1.0 - value
        else:
            self._source_value = value

    def __repr__(self):
        return f"<{self.__class__.__name__}(info={self.info})>"
