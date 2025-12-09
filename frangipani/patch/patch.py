from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from frangipani.patch.patch_address import PatchAddress
from frangipani.patch.patch_item import PatchItem


@dataclass_json
@dataclass
class Patch:
    name: str
    items: list[PatchItem] = field(default_factory=list)

    def get_by_address(self, address: PatchAddress) -> PatchItem | None:
        for item in self.items:
            if item.address == address:
                return item

        return None
