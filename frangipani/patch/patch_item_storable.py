from dataclasses import dataclass

from dataclasses_json import dataclass_json

from frangipani.patch.patch_address import PatchAddress


@dataclass_json
@dataclass
class PatchItemStorable:
    address: PatchAddress
    definition_identifier: str
    name: str
    tags: list[str]
