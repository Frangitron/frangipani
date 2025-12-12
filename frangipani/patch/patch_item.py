from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from frangipani.fixture.definition.definition import FixtureDefinition
from frangipani.patch.patch_address import PatchAddress


@dataclass_json
@dataclass
class PatchItem:
    address: PatchAddress
    name: str
    tags: list[str]
    definition: FixtureDefinition | None = None
    _parameter_values: dict[str, float] = field(default_factory=dict)

    def __post_init__(self):
        self.at_default()

    def set_parameter(self, name: str, value: float, opacity: float) -> None:
        self._parameter_values[name] = min(max(0.0, value * opacity + self._parameter_values[name] * (1 - opacity)), 1.0)

    def get_parameter(self, name: str) -> float:
        return self._parameter_values[name]

    def at_zero(self):
        for parameter in self.definition.parameter_definitions:
            self._parameter_values[parameter.name] = 0.0

    def at_default(self):
        for parameter in self.definition.parameter_definitions:
            self._parameter_values[parameter.name] = parameter.default_value
