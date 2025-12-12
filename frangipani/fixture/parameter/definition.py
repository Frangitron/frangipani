from dataclasses import dataclass

from dataclasses_json import dataclass_json

from frangipani.fixture.parameter.resolution import ParameterResolution
from frangipani.fixture.parameter.type import ParameterType


@dataclass_json
@dataclass
class FixtureParameterDefinition:
    address: int
    default_value: tuple[float, ...]
    name: str
    resolution: ParameterResolution
    type: ParameterType
