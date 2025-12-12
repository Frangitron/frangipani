from dataclasses import dataclass

from dataclasses_json import dataclass_json

from frangipani.fixture.parameter.definition import FixtureParameterDefinition


@dataclass_json
@dataclass
class FixtureDefinition:
    parameter_definitions: list[FixtureParameterDefinition]
    manufacturer: str
    model: str

    @property
    def identifier(self) -> str:
        return f"{self.manufacturer}#{self.model}"
