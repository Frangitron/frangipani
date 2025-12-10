from dataclasses import dataclass

from dataclasses_json import dataclass_json

from frangipani.layer.scope.base import BaseLayerScope


@dataclass_json
@dataclass
class LayerScopeAll(BaseLayerScope):

    def is_matching(self, scope: BaseLayerScope) -> bool:
        return True
