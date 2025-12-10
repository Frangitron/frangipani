from abc import ABC, abstractmethod

from frangipani.patch.patch import Patch
from frangipani.patch.patch_address import PatchAddress
from frangipani.patch.patch_item import PatchItem


class IPatchStore(ABC):
    def __init__(self):
        self._patch: Patch = Patch(
            name="Internal",
        )

    @abstractmethod
    def load(self, identifier: str) -> None:
        pass

    @abstractmethod
    def save(self, identifier: str, name: str = None) -> None:
        pass

    @abstractmethod
    def get_by_address(self, address: PatchAddress) -> PatchItem | None:
        pass

    def set_patch(self, patch: Patch) -> None:
        self._patch = patch

    @property
    def items(self) -> list[PatchItem]:
        return self._patch.items

    # TODO: check if pertinent to mix abstract and domain in same class
    # spoiler alert: probably not
    def list_universes(self) -> list[int]:
        universes = list()
        for item in self._patch.items:
            if item.address.universe not in universes:
                universes.append(item.address.universe)

        return sorted(universes)
