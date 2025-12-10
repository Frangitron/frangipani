from dataclasses import dataclass

from dataclasses_json import dataclass_json

from frangipani.layer.scope.base import BaseLayerScope
from frangipani.patch.patch_item import PatchItem


@dataclass_json
@dataclass
class LayerScopeTag(BaseLayerScope):
    tags: list[str]

    def is_matching(self, patch_item: PatchItem) -> bool:
        scope_tags = {tag.lower() for tag in self.tags}
        item_tags = {tag.lower() for tag in patch_item.tags}
        return scope_tags.issubset(item_tags)
