from enum import StrEnum

from frangipani.fixture.parameter.channel.channel_kind import FixtureParameterChannelKind


class ParameterType(StrEnum):
    Dimmer = "dimmer"
    ColorRGB = "color_rgb"

    @property
    def channel_kinds(self) -> tuple[FixtureParameterChannelKind]:
        return {
            ParameterType.Dimmer: (
                FixtureParameterChannelKind.Dimmer,
            ),
            ParameterType.ColorRGB: (
                FixtureParameterChannelKind.Red,
                FixtureParameterChannelKind.Green,
                FixtureParameterChannelKind.Blue
            ),
        }[self]
