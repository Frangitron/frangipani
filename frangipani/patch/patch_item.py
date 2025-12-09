from dataclasses import dataclass

from dataclasses_json import dataclass_json

from frangipani.fixture_definition.fixture_definition import FixtureDefinition
from frangipani.patch.patch_address import PatchAddress


@dataclass_json
@dataclass
class PatchItem:
    address: PatchAddress
    name: str
    tags: list[str]
    definition: FixtureDefinition | None = None

