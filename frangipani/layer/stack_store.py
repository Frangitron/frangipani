from abc import ABC, abstractmethod

from frangipani.layer import Layer
from frangipani.layer.stack import LayerStack


class ILayerStackStore(ABC):
    def __init__(self):
        self._stack: LayerStack = LayerStack(name="Internal")

    @abstractmethod
    def load(self, identifier: str) -> None:
        pass

    @abstractmethod
    def save(self, identifier: str) -> None:
        pass

    def set_stack(self, stack: LayerStack) -> None:
        self._stack = stack

    @property
    def layers(self) -> list[Layer]:
        return self._stack.layers
