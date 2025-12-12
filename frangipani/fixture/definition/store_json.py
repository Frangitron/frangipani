import json
import logging
from importlib import resources

from frangipani.fixture.definition.definition import FixtureDefinition
from frangipani.fixture.definition.library import FixtureDefinitionLibrary
from frangipani.fixture.definition.store import IFixtureDefinitionStore

_logger = logging.getLogger("FixtureDefinitionStore")


class JsonFixtureDefinitionStore(IFixtureDefinitionStore):

    def __init__(self):
        self._library: FixtureDefinitionLibrary = FixtureDefinitionLibrary(
            name="Internal"
        )

    def load(self, identifier: str) -> None:
        _logger.info(f"Loading definitions from '{identifier}'")

        with (open(identifier, "r") as file):
            library = FixtureDefinitionLibrary.from_json(file.read())

        if library.api_version != FixtureDefinitionLibrary.api_version:
            raise Exception(
                f"Library '{library.name}'. Incompatible API version: "
                f"{library.api_version} (should be {FixtureDefinitionLibrary.api_version})"
            )

        self._library = library

    def save(self, identifier: str) -> None:
        _logger.info(f"Saving definitions to '{identifier}'")

        data = self._library.to_dict()
        data['api_version'] = self._library.api_version
        with open(identifier, "w") as file:
            json.dump(data, file, indent=2)

        _logger.info(f"Saved {len(self._library.definitions)} definitions to '{identifier}'")

    def get_by_identifier(self, identifier: str) -> FixtureDefinition | None:
        for definition in self._library.definitions:
            if definition.identifier == identifier:
                return definition

        return None

    def set_library(self, library: FixtureDefinitionLibrary):
        self._library = library

    def load_default_library(self):
        self.load(self.make_generic_libray_filepath())

    @staticmethod
    def make_generic_libray_filepath() -> str:
        with resources.path("frangipani.resources.fixture_definition_libraries", "generic.json") as path:
            return str(path)
