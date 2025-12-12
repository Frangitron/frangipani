import fnmatch

from pythonhelpers.injector import Injector

from frangipani.driver.driver import Driver
from frangipani.driver.pool_store import IDriverPoolStore
from frangipani.fixture.parameter.channel.channel import FixtureParameterChannel
from frangipani.fixture.parameter.channel.channel_kind import FixtureParameterChannelKind
from frangipani.fixture.parameter.definition import FixtureParameterDefinition
from frangipani.layer.layer import Layer
from frangipani.layer.scope.base import BaseLayerScope
from frangipani.layer.stack_store import ILayerStackStore
from frangipani.layer.value.base import BaseLayerValue
from frangipani.math.interpolator import Interpolator
from frangipani.patch.patch_item import PatchItem
from frangipani.patch.store import IPatchStore


class Resolver:

    def __init__(self):
        self._patch_store = Injector().inject(IPatchStore)
        self._driver_pool_store = Injector().inject(IDriverPoolStore)
        self._layer_stack_store = Injector().inject(ILayerStackStore)

    def patch_items_for_scope(self, scope: BaseLayerScope) -> list[PatchItem]:
        resolved_items = list()
        for patch_item in self._patch_store.items:
            if scope.is_matching(patch_item):
                resolved_items.append(patch_item)

        return resolved_items

    @staticmethod
    def fixture_parameter_definitions_for_layer_value(patch_item: PatchItem, layer_value: BaseLayerValue) -> list[FixtureParameterDefinition]:
        parameter_definitions = list()

        for parameter in patch_item.definition.parameter_definitions:
            if fnmatch.fnmatch(parameter.name.lower(), layer_value.parameter_selector.lower()):
                parameter_definitions.append(parameter)

        return parameter_definitions

    def parameter_definitions_for_driver(self, driver: Driver) -> list[FixtureParameterDefinition]:
        if driver.info.target_identifier.targets_opacity:
            return list()

        driver_parameters = list()
        for layer in self._layer_stack_store.layers:
            if driver.info.target_identifier.is_matching(layer):
                patch_items = self.patch_items_for_scope(layer.scope)

                for value in layer.values:
                    if driver.info.target_identifier.value_name == value.name:
                        for patch_item in patch_items:
                            driver_parameters.extend(
                                self.fixture_parameter_definitions_for_layer_value(patch_item, value)
                            )

        return driver_parameters

    def resolve_all_driver_channels(self):
        for driver in self._driver_pool_store.drivers:
            self.resolve_driver_channels(driver)

    # TODO split in several methods (list, validate, assign/create channels)
    def resolve_driver_channels(self, driver: Driver):
        if driver.info.target_identifier.targets_opacity:
            driver.channels = [FixtureParameterChannel(
                kind=FixtureParameterChannelKind.LayerOpacity,
                interpolator=Interpolator(
                    fade_in_time=driver.info.fade_in_time,
                    fade_out_time=driver.info.fade_out_time
                ))]
            return

        parameter_definitions = self.parameter_definitions_for_driver(driver)
        channel_kinds = list()
        for parameter_definition in parameter_definitions:
            channel_kinds.append(parameter_definition.type.channel_kinds)

        channel_kinds = list(set(channel_kinds))
        if len(channel_kinds) > 1:
            raise ValueError(
                f"Inconsistent channel kinds for driver {driver.info.name}:"
                f" {', '.join([k.name for k in channel_kinds])}"
            )

        for channel_kind in channel_kinds[0]:
            new_channel = FixtureParameterChannel(
                kind=channel_kind,
                interpolator=Interpolator(
                    fade_in_time=driver.info.fade_in_time,
                    fade_out_time=driver.info.fade_out_time
                )
            )
            driver.channels.append(new_channel)

    def drivers_for_layer(self, layer: Layer) -> list[Driver]:
        drivers = list()
        for driver in self._driver_pool_store.drivers:
            if driver.info.target_identifier.is_matching(layer):
                drivers.append(driver)

        return drivers
