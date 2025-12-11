import fnmatch

from pythonhelpers.injector import Injector

from frangipani.engine.resolver import Resolver
from frangipani.layer.stack_store import ILayerStackStore
from frangipani.patch import IPatchStore


def _match(selector: str, name: str) -> bool:
    return fnmatch.fnmatch(name.lower(), selector.lower())


class Solver:

    def __init__(self):
        self._layer_stack_store = Injector().inject(ILayerStackStore)
        self._patch_store = Injector().inject(IPatchStore)
        self._resolver = Resolver()
        self._universe_buffers: dict[int, bytearray] = {}

    def initialize(self):
        print(f"Layers in stack : {len(self._layer_stack_store.layers)}")

        for patch_item in self._patch_store.items:
            if patch_item.address.universe not in self._universe_buffers:
                self._universe_buffers[patch_item.address.universe] = bytearray(512)

        print(f"DMX universes : {len(self._universe_buffers)}")
        print("Solver initialized")

    def solve(self):
        for patch_item in self._patch_store.items:
            patch_item.at_zero()

        for layer in self._layer_stack_store.layers:
            patch_items = self._resolver.patch_items_for_scope(layer.scope)
            drivers = self._resolver.drivers_for_layer(layer)

            for driver in drivers:
                if not driver.enabled:
                    continue

                if driver.target_identifier.targets_opacity:
                    layer.opacity = driver.source_value

                else:
                    layer.set_value(
                        name=driver.target_identifier.value_name,
                        new_value=driver.source_value
                    )

            for value in layer.values:
                for patch_item in patch_items:
                    for parameter_definition in patch_item.definition.parameter_definitions:
                        if _match(value.parameter_selector, parameter_definition.name):
                            patch_item.set_parameter(
                                name=parameter_definition.name,
                                value=value.value,
                                opacity=layer.opacity
                            )

        for patch_item in self._patch_store.items:
            for parameter_definition in patch_item.definition.parameter_definitions:
                scalar = patch_item.get_parameter(parameter_definition.name)
                address = patch_item.address.channel + parameter_definition.address - 1
                self._universe_buffers[patch_item.address.universe][address] = int(scalar * 255)

    def get_dmx_buffer(self, universe: int) -> bytearray:
        return self._universe_buffers[universe]
