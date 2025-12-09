from abc import ABC, abstractmethod

from frangipani.patch.patch import Patch
from frangipani.patch.patch_address import PatchAddress
from frangipani.patch.patch_item import PatchItem


class IPatchStore(ABC):

    @abstractmethod
    def load(self, identifier: str) -> None:
        pass

    @abstractmethod
    def save(self, identifier: str, name: str = None) -> None:
        pass

    @abstractmethod
    def set_patch(self, patch: Patch) -> None:
        pass

    @abstractmethod
    def get_by_address(self, address: PatchAddress) -> PatchItem | None:
        pass
