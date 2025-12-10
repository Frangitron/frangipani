import logging

from pythonhelpers.injector import Injector

from frangipani.fixture_definition import (
    IFixtureDefinitionStore,
    JsonFixtureDefinitionStore,
)
from frangipani.patch import (
    Patch,
    PatchAddress,
    PatchItem,
    JsonPatchStore,
)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    _logger = logging.getLogger("Script:MakeDemoPatch")

    fixture_definition_store = JsonFixtureDefinitionStore()
    fixture_definition_store.load_default_library()

    Injector().set_dependencies({
        IFixtureDefinitionStore: fixture_definition_store,
    })

    dimmer_definition = fixture_definition_store.get_by_identifier("Generic#Dimmer 1 Channel")
    assert dimmer_definition is not None

    rgb_color_definition = fixture_definition_store.get_by_identifier("Generic#Color RGB")
    assert rgb_color_definition is not None

    patch = Patch(
        name="Demo Patch",
        items=[
            PatchItem(
                address=PatchAddress(universe=1, channel=1),
                name="Dimmer 1",
                tags=["Dimmer", "Odd"],
                definition=dimmer_definition
            ),
            PatchItem(
                address=PatchAddress(universe=1, channel=2),
                name="Dimmer 2",
                tags=["Dimmer", "Even"],
                definition=dimmer_definition
            ),
            PatchItem(
                address=PatchAddress(universe=1, channel=3),
                name="RGB 1",
                tags=["RGB", "Odd"],
                definition=rgb_color_definition
            ),
            PatchItem(
                address=PatchAddress(universe=1, channel=6),
                name="RGB 1",
                tags=["RGB", "Even"],
                definition=rgb_color_definition
            ),
        ],
    )

    patch_store = JsonPatchStore()
    patch_store.set_patch(patch)
    patch_store.save("demo.patch.json")

    _logger.info("Test loading back")
    patch_store = JsonPatchStore()
    patch_store.load("demo.patch.json")

    for item in patch.items:
        assert item == patch_store.get_by_address(item.address)
