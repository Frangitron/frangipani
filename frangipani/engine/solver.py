from pythonhelpers.injector import Injector

from frangipani.engine.resolver import Resolver
from frangipani.layer.stack_store import ILayerStackStore
from frangipani.patch import IPatchStore


class Solver:

    def __init__(self):
        self._layer_stack_store = Injector().inject(ILayerStackStore)
        self._patch_store = Injector().inject(IPatchStore)
        self._resolver = Resolver()
        self._universe_buffers: dict[int, bytearray] = {}

    def clear(self):
        self._universe_buffers.clear()

    def initialize(self):
        print(f"Layers in stack : {len(self._layer_stack_store.layers)}")

        for patch_item in self._patch_store.items:
            if patch_item.address.universe not in self._universe_buffers:
                self._universe_buffers[patch_item.address.universe] = bytearray(512)

        self._resolver.resolve_all_driver_channels()
        print(f"All Driver channels resolved")

        print(f"DMX universes : {len(self._universe_buffers)}")
        print("Solver initialized")

    def solve(self):
        for patch_item in self._patch_store.items:
            patch_item.at_zero()

        for layer in self._layer_stack_store.layers:
            patch_items = self._resolver.patch_items_for_scope(layer.scope)
            drivers = self._resolver.drivers_for_layer(layer)

            for driver in drivers:
                if not driver.info.enabled:
                    continue

                if driver.info.target_identifier.targets_opacity:
                    layer.opacity = driver.value[0]

                else:
                    layer.set_value_from_channels(
                        value_name=driver.info.target_identifier.value_name,
                        channel_values=driver.value
                    )

            for layer_value in layer.values:
                for patch_item in patch_items:
                    parameter_definitions = self._resolver.fixture_parameter_definitions_for_layer_value(
                        patch_item=patch_item,
                        layer_value=layer_value
                    )
                    for parameter_definition in parameter_definitions:
                        patch_item.set_parameter(
                            name=parameter_definition.name,
                            value=layer_value.value,
                            opacity=layer.opacity
                        )

        for patch_item in self._patch_store.items:
            for parameter_definition in patch_item.definition.parameter_definitions:
                scalar = patch_item.get_parameter(parameter_definition.name)
                address = patch_item.address.channel + parameter_definition.address - 1
                self._universe_buffers[patch_item.address.universe][address] = int(round(scalar * 255))

    def get_dmx_buffer(self, universe: int) -> bytearray:
        return self._universe_buffers[universe]
