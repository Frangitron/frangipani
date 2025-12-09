import json
import logging
import os

from pyside6helpers import resources

from frangipani.fixture_definition.fixture_definition import FixtureDefinition
from frangipani.fixture_definition.fixture_definition_library import FixtureDefinitionLibrary


_logger = logging.getLogger("FixtureDefinitionStore")


class FixtureDefinitionStore:

    def __init__(self):
        self._definitions: dict[str, FixtureDefinition] = {}

    def load(self) -> list[FixtureDefinition]:
        self._definitions = {}

        generic_filepath = resources.find(os.path.join("fixture_definition_libraries", "generic.json"))
        self._definitions.update(FixtureDefinitionStore.load_library_file(generic_filepath))

        self._definitions = dict(sorted(self._definitions.items(), key=lambda items: items[1].identifier))
        return list(self._definitions.values())

    def save(self, library: FixtureDefinitionLibrary, filepath: str) -> None:
        _logger.info(f"Saving definitions to '{filepath}'")

        data = library.to_dict()
        data['api_version'] = library.api_version
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)

        _logger.info(f"Saved {len(library.definitions)} definitions to '{filepath}'")

    @staticmethod
    def load_library_file(filepath: str) -> FixtureDefinitionLibrary:
        _logger.info(f"Loading definitions from '{filepath}'")
        identifiers: list[str] = []

        with open(filepath, "r") as f:
            library = FixtureDefinitionLibrary.from_json(f.read())

        if library.api_version != FixtureDefinitionLibrary.api_version:
            raise Exception(f"Library '{library.name}'. Incompatible API version: {library.api_version}")

        for fixture_definition in library.definitions:
            if fixture_definition.identifier in identifiers:
                raise Exception(f"Library '{library.name}'. Fixture already defined: {fixture_definition}")

            identifiers.append(fixture_definition.identifier)

        _logger.info(f"Loaded {len(library.definitions)} definitions")

        return library
