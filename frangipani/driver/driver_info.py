from dataclasses import dataclass

from dataclasses_json import dataclass_json

from frangipani.driver.source_identifier import DriverSourceIdentifier
from frangipani.driver.target_identifier import DriverTargetIdentifier
from frangipani.fixture.parameter.channel import FixtureParameterChannelKind


@dataclass_json
@dataclass
class DriverInfo:
    name: str
    target_identifier: DriverTargetIdentifier
    source_identifier: DriverSourceIdentifier

    enabled: bool = True
    fade_in_time: float = 0.0
    fade_out_time: float = 0.0
    inverted: bool = False
