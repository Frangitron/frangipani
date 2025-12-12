from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

from frangipani.fixture.parameter.channel.channel_kind import FixtureParameterChannelKind
from frangipani.math.interpolator import Interpolator


@dataclass_json
@dataclass
class FixtureParameterChannel:
    kind: FixtureParameterChannelKind
    interpolator: Interpolator
