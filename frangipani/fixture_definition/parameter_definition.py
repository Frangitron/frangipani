from dataclasses import dataclass

from dataclasses_json import dataclass_json

from frangipani.fixture_definition.parameter_resolution_enum import ParameterResolutionEnum
from frangipani.fixture_definition.parameter_type_enum import ParameterTypeEnum


@dataclass_json
@dataclass
class ParameterDefinition:
    address: int
    default_value: float
    name: str
    resolution: ParameterResolutionEnum
    type: ParameterTypeEnum
