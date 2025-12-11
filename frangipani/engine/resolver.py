from pythonhelpers.injector import Injector

from frangipani.driver.driver import Driver
from frangipani.driver.pool_store import IDriverPoolStore
from frangipani.layer.layer import Layer
from frangipani.layer.scope.base import BaseLayerScope
from frangipani.patch.patch_item import PatchItem
from frangipani.patch.store import IPatchStore


class Resolver:

    def __init__(self):
        self._patch_store = Injector().inject(IPatchStore)
        self._driver_pool_store = Injector().inject(IDriverPoolStore)

    def patch_items_for_scope(self, scope: BaseLayerScope) -> list[PatchItem]:
        resolved_items = list()
        for patch_item in self._patch_store.items:
            if scope.is_matching(patch_item):
                resolved_items.append(patch_item)

        return resolved_items

    def drivers_for_layer(self, layer: Layer) -> list[Driver]:
        drivers = list()
        for driver in self._driver_pool_store.drivers:
            if driver.target_identifier.is_matching(layer):
                drivers.append(driver)

        return drivers
