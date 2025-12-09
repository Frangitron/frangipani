from dataclasses import dataclass, field
from typing import ClassVar

from dataclasses_json import dataclass_json

from frangipani.fixture_definition.fixture_definition import FixtureDefinition


@dataclass_json
@dataclass
class FixtureDefinitionLibrary:
    name: str
    api_version: ClassVar[int] = 1
    definitions: list[FixtureDefinition] = field(default_factory=list)
