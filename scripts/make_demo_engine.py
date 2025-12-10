import logging

from pythonhelpers.injector import Injector

from frangipani.driver import (
    IDriverStore,
    JsonDriverStore,
)
from frangipani.engine import (
    Engine,
    EngineConfiguration,
)
from frangipani.fixture_definition import (
    IFixtureDefinitionStore,
    JsonFixtureDefinitionStore,
)
from frangipani.layer import (
    ILayerStackStore,
    JsonLayerStackStore,
)
from frangipani.patch import (
    IPatchStore,
    JsonPatchStore,
)


if __name__ == "__main__":

    #
    # Init
    logger = logging.getLogger("Script:DemoEngine")

    #
    # Fixture definitions
    fixture_definition_store = JsonFixtureDefinitionStore()
    fixture_definition_store.load_default_library()
    Injector().set_dependencies({
        IFixtureDefinitionStore: fixture_definition_store,
    })

    #
    # Patch
    patch_store = JsonPatchStore()
    patch_store.load("demo.patch.json")
    Injector().set_dependencies({
        IPatchStore: patch_store,
    })

    #
    # Layer stack
    layer_stack_store = JsonLayerStackStore()
    layer_stack_store.load("demo.layerstack.json")
    Injector().set_dependencies({
        ILayerStackStore: layer_stack_store
    })

    #
    # Drivers
    driver_store = JsonDriverStore()
    driver_store.load("demo.drivers.json")
    Injector().set_dependencies({
        IDriverStore: driver_store
    })

    #
    # Engine
    engine = Engine(EngineConfiguration(
        artnet_target_ip='127.0.0.1'
    ))
    engine.initialize()

    try:
        engine.main_loop()
    except KeyboardInterrupt:
        engine.stop()
