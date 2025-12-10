from abc import ABC, abstractmethod

from frangipani.layer.stack import LayerStack


class ILayerStackStore(ABC):

    @abstractmethod
    def load(self, identifier: str) -> None:
        pass

    @abstractmethod
    def save(self, identifier: str) -> None:
        pass

    @abstractmethod
    def set_stack(self, stack: LayerStack) -> None:
        pass

    @property
    @abstractmethod
    def stack(self) -> LayerStack:
        pass
