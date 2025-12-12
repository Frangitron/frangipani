from abc import ABC, abstractmethod

from frangipani.fixture.definition.definition import FixtureDefinition
from frangipani.fixture.definition.library import FixtureDefinitionLibrary


class IFixtureDefinitionStore(ABC):

    @abstractmethod
    def load(self, identifier: str) -> None:
        pass

    @abstractmethod
    def save(self, identifier: str) -> None:
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
