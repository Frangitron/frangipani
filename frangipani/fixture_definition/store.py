from abc import ABC, abstractmethod

from frangipani.fixture_definition.fixture_definition import FixtureDefinition
from frangipani.fixture_definition.fixture_definition_library import FixtureDefinitionLibrary


class IFixtureDefinitionStore(ABC):

    @abstractmethod
    def load(self, identifier: str) -> None:
        pass

    @abstractmethod
    def save(self, library: FixtureDefinitionLibrary, identifier: str) -> None:
        pass

    @abstractmethod
    def get_by_identifier(self, identifier: str) -> FixtureDefinition | None:
        pass

    @abstractmethod
    def set_library(self, library: FixtureDefinitionLibrary) -> None:
        pass

    @abstractmethod
    def load_default_library(self) -> None:
        pass
