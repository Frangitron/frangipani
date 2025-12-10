from frangipani.layer.stack import LayerStack
from frangipani.layer.stack_store import ILayerStackStore


class JsonLayerStackStore(ILayerStackStore):

    def __init__(self):
        self._stack: LayerStack = LayerStack(name="Internal")

    def load(self, identifier: str) -> None:
        with open(identifier, 'r') as file:
            self._stack = LayerStack.from_json(file.read())

    def save(self, identifier: str) -> None:
        with open(identifier, 'w') as file:
            file.write(self._stack.to_json(indent=2))

    def set_stack(self, stack: LayerStack) -> None:
        self._stack = stack

    @property
    def stack(self) -> LayerStack:
        return self._stack
