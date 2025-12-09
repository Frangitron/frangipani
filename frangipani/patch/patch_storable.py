from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from frangipani.patch.patch import Patch
from frangipani.patch.patch_item_converter import PatchItemConverter
from frangipani.patch.patch_item_storable import PatchItemStorable


@dataclass_json
@dataclass
class PatchStorable:
    name: str
    items: list[PatchItemStorable] = field(default_factory=list)

    @staticmethod
    def from_patch(patch: Patch) -> "PatchStorable":
        patch_storable = PatchStorable(name=patch.name)
        for item in patch.items:
            item_storable: PatchItemStorable = PatchItemConverter.to_storable(item)
            patch_storable.items.append(item_storable)

        return patch_storable
