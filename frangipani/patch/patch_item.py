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
    _parameter_values: dict[str, tuple[float, ...]] = field(default_factory=dict)

    def __post_init__(self):
        self.at_default()

    def set_parameter_value(self, name: str, value: tuple[float, ...], opacity: float) -> None:
        # FIXME edge case where layer selector is All and value has 1 channel :/
        channel_count = len(self.definition.parameter_by_name(name).type.channel_kinds)
        if len(value) == 1 and channel_count > 1:
            value = [value[0]] * channel_count

        channel_values = []
        for channel_index, channel_value in enumerate(value):
            channel_values.append(min(max(0.0, channel_value * opacity + self._parameter_values[name][channel_index] * (1 - opacity)), 1.0))

        self._parameter_values[name] = tuple(channel_values)

    def get_parameter_value(self, name: str) -> tuple[float, ...]:
        return self._parameter_values[name]

    def at_zero(self):
        for parameter in self.definition.parameter_definitions:
            self._parameter_values[parameter.name] = tuple(0.0 for _ in range(len(parameter.type.channel_kinds)))

    def at_default(self):
        for parameter in self.definition.parameter_definitions:
            self._parameter_values[parameter.name] = parameter.default_value
