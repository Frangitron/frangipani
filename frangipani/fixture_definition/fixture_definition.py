from dataclasses import dataclass

from dataclasses_json import dataclass_json

from frangipani.fixture_definition.parameter_definition import ParameterDefinition


@dataclass_json
@dataclass
class FixtureDefinition:
    parameter_definitions: list[ParameterDefinition]
    manufacturer: str
    model: str

    @property
    def identifier(self) -> str:
        return f"{self.manufacturer}#{self.model}"
