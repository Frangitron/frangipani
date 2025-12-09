from pythonhelpers.injector import Injector

from frangipani.fixture_definition import IFixtureDefinitionStore
from frangipani.patch.patch_item import PatchItem
from frangipani.patch.patch_item_storable import PatchItemStorable


class PatchItemConverter:

    @staticmethod
    def from_storable(item_storable: PatchItemStorable) -> PatchItem:
        fixture_definition_store: IFixtureDefinitionStore = Injector().inject(IFixtureDefinitionStore)
        return PatchItem(
            address=item_storable.address,
            name=item_storable.name,
            tags=item_storable.tags,
            definition=fixture_definition_store.get_by_identifier(item_storable.definition_identifier),
        )

    @staticmethod
    def to_storable(item: PatchItem) -> PatchItemStorable:
        return PatchItemStorable(
            address=item.address,
            definition_identifier=item.definition.identifier,
            name=item.name,
            tags=item.tags,
        )
