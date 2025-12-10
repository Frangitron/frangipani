from dataclasses import dataclass

from dataclasses_json import dataclass_json

from frangipani.layer.value.base import BaseLayerValue


@dataclass_json
@dataclass
class LayerValueScalar(BaseLayerValue[float]):
    pass
