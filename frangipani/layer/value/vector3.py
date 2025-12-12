from dataclasses import dataclass

from dataclasses_json import dataclass_json

from frangipani.layer.value.base import BaseLayerValue


@dataclass_json
@dataclass
class LayerValueVector3(BaseLayerValue[tuple[float, float, float]]):

    def set_value_from_channels(self, channel_values: tuple[float, ...]) -> None:
        if len(channel_values) != 3:
            raise ValueError(f"{self} expects 3 values, got {len(channel_values)}, is Driver bound to right control type ?")

        self.value = channel_values
