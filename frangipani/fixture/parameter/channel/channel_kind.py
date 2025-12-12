from enum import StrEnum, auto


class FixtureParameterChannelKind(StrEnum):
    LayerOpacity = auto()  # FIXME this is not a FixtureParameterChannelKind anymore
    Amber = auto()
    Blue = auto()
    Dimmer = auto()
    Green = auto()
    Pan = auto()
    Red = auto()
    Tilt = auto()
    UV = auto()
    White = auto()
    WhiteCold = auto()
    WhiteWarm = auto()
