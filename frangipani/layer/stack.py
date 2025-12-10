from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from frangipani.layer.layer import Layer


@dataclass_json
@dataclass
class LayerStack:
    name: str
    layers: list[Layer] = field(default_factory=list)
