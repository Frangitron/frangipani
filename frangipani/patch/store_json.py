import logging

from pythonhelpers.injector import Injector

from frangipani.fixture_definition.store import IFixtureDefinitionStore
from frangipani.patch.patch import Patch
from frangipani.patch.patch_address import PatchAddress
from frangipani.patch.patch_item import PatchItem
from frangipani.patch.patch_item_converter import PatchItemConverter
from frangipani.patch.patch_storable import PatchStorable
from frangipani.patch.store import IPatchStore

_logger = logging.getLogger("PatchStore")


class JsonPatchStore(IPatchStore):

    def load(self, identifier: str) -> None:
        _logger.info(f"Loading patch from '{identifier}'")

        with open(identifier, "r") as file:
            patch_storable: PatchStorable = PatchStorable.from_json(file.read())

        for item_storable in patch_storable.items:
            item_at_address = self._patch.get_by_address(item_storable.address)
            if item_at_address is not None:
                raise Exception(
                    f"Duplicate address ({item_storable.address}) "
                    f"between '{item_storable.name}' "
                    f"and '{item_at_address.name}'"
                )

            self._patch.items.append(
                PatchItemConverter.from_storable(item_storable)
            )

        _logger.info(f"Loaded {len(patch_storable.items)} items from stored patch '{patch_storable.name}'")

    def save(self, identifier: str, name: str = None) -> None:
        _logger.info(f"Saving patch to '{identifier}'")
        if name is not None:
            self._patch.name = name

        patch_storable: PatchStorable = PatchStorable.from_patch(self._patch)
        with open(identifier, "w") as file:
            file.write(patch_storable.to_json(indent=2))

    def get_by_address(self, address: PatchAddress) -> PatchItem | None:
        for item in self._patch.items:
            if item.address == address:
                return item

        return None
