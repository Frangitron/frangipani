from dataclasses import dataclass, field

from dataclasses_json import dataclass_json, config

from pythonhelpers.dataclass_json_inheritance_codec import DataclassJsonInheritanceCodec

from frangipani.layer.scope.base import BaseLayerScope
from frangipani.layer.value.base import BaseLayerValue


_BaseLayerValueCodec = DataclassJsonInheritanceCodec[BaseLayerValue]
_BaseScopeCodec = DataclassJsonInheritanceCodec[BaseLayerScope]


@dataclass_json
@dataclass
class Layer:
    name: str
    scope: BaseLayerScope = field(metadata=config(
        decoder=lambda scope: _BaseScopeCodec.decode(scope, BaseLayerScope),
        encoder=_BaseScopeCodec.encode
    ))
    opacity: float = 1.0
    values: list[BaseLayerValue] = field(
        default_factory=list,
        metadata=config(
            decoder=lambda values_data: [
                _BaseLayerValueCodec.decode(value_data, BaseLayerValue) for value_data in values_data
            ],
            encoder=lambda values: [
                _BaseLayerValueCodec.encode(value) for value in values
            ]
        )
    )
