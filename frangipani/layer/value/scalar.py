from dataclasses import dataclass

from dataclasses_json import dataclass_json

from frangipani.layer.value.base import BaseLayerValue


@dataclass_json
@dataclass
class LayerValueScalar(BaseLayerValue[float]):

    def set_value_from_channels(self, channel_values: tuple[float, ...]) -> None:
        if len(channel_values) != 1:
            raise ValueError(f"Expected 1 value, got {len(channel_values)}")

        self.value = channel_values[0]
