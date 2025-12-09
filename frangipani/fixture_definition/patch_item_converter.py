from frangipani.patch.patch_item import PatchItem
from frangipani.patch.patch_item_storable import PatchItemStorable


def item_from_storable(self, item_storable: PatchItemStorable) -> PatchItem:
    return PatchItem(
        address=item_storable.address,
        name=item_storable.name,
        tags=item_storable.tags,
    )



def item_to_storable(self, item: PatchItem) -> PatchItemStorable:
    return PatchItemStorable(
        address=item.address,
        definition_identifier=item.definition.identifier,
        name=item.name,
        tags=item.tags,
    )
