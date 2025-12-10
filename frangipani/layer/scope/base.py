from abc import ABC, abstractmethod
from dataclasses import dataclass

from dataclasses_json import dataclass_json

from frangipani.patch.patch_item import PatchItem


@dataclass_json
@dataclass
class BaseLayerScope(ABC):

    @abstractmethod
    def is_matching(self, patch_item: PatchItem) -> bool:
        pass
