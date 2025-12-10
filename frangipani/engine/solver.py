from pythonhelpers.injector import Injector

from frangipani.engine.resolver import Resolver
from frangipani.layer.stack_store import ILayerStackStore


class Solver:

    def __init__(self):
        self._layer_stack_store = Injector().inject(ILayerStackStore)
        self._resolver = Resolver()

    def initialize(self):
        print(f"Layers in stack : {len(self._layer_stack_store.layers)}")
        print("Solver initialized")

    def solve(self):
        print(">> Solving layers...")
        for layer in self._layer_stack_store.layers:
            patch_items = self._resolver.patch_items_for_scope(layer.scope)
            drivers = self._resolver.drivers_for_layer(layer)

            print(f"> Solving layer {layer.name}")
            print(f"Patch items: {[patch_item.name for patch_item in patch_items]}")
            print(f"Drivers: {[driver.name for driver in drivers]}")

    def get_dmx_buffer(self, universe: int) -> bytearray:
        return bytearray(512)
