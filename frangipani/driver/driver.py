from frangipani.driver.driver_info import DriverInfo
from frangipani.fixture.parameter.channel import FixtureParameterChannelKind
from frangipani.fixture.parameter.channel.channel import FixtureParameterChannel


class Driver:
    def __init__(self, info: DriverInfo):
        self.info = info
        self._source_value: tuple[float, ...] | None = None
        self._previous_value: tuple[float, ...] | None = None
        self._interpolated_value: tuple[float, ...] | None = None
        self.channels: list[FixtureParameterChannel] = []

    def compute_value(self) -> None:
        interpolated_value = [0.0 for _ in self.channels]

        for channel_index, channel in enumerate(self.channels):
            interpolated = channel.interpolator.value
            interpolated_value[channel_index] = 1.0 - interpolated if self.info.inverted else interpolated

        self._interpolated_value = tuple(interpolated_value)

    @property
    def value(self) -> tuple[float, ...]:
        self.compute_value()
        return self._interpolated_value

    def set_source_value(self, value: tuple[float, ...]) -> None:
        # FIXME Hack to make Hue/Saturation conversion to RGB
        kinds = {channel.kind for channel in self.channels}
        if kinds == {FixtureParameterChannelKind.Red, FixtureParameterChannelKind.Green, FixtureParameterChannelKind.Blue}:
            value = (value[0], value[1], 0.0)

        if len(value) != len(self.channels):
            raise ValueError(
                f"Expected {len(self.channels)} value(s), got {len(value)} for driver {self.info.name}"
            )
        if value is not None:
            self._source_value = tuple(min(max(0.0, float(value_item)), 1.0) for value_item in value)

            if self._previous_value != self._source_value:
                self._previous_value = self._source_value
                for channel_index, channel in enumerate(self.channels):
                    channel.interpolator.set_target(self._source_value[channel_index])

    def __repr__(self):
        return f"<{self.__class__.__name__}(info={self.info})>"
