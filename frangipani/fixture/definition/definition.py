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

    def parameter_by_name(self, name: str) -> FixtureParameterDefinition:
        try:
            return next(filter(lambda p: p.name == name, self.parameter_definitions))
        except StopIteration:
            raise ValueError(f"Parameter '{name}' not found in fixture definition")
