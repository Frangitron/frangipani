import logging

from frangipani.fixture.definition import (
    FixtureDefinition,
    FixtureDefinitionLibrary,
    JsonFixtureDefinitionStore,
)
from frangipani.fixture.parameter import (
    FixtureParameterDefinition,
    ParameterResolution,
    ParameterType,
)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    _logger = logging.getLogger("Script:GenericFixtureDefinitions")
    _logger.info("Creating generic fixture definition library")

    library = FixtureDefinitionLibrary(
        name="Generic Fixture Definitions",
        definitions=[
            FixtureDefinition(
                parameter_definitions=[
                    FixtureParameterDefinition(
                        address=0,
                        default_value=0.0,
                        name="Dimmer",
                        resolution=ParameterResolution.Simple,
                        type=ParameterType.Dimmer
                    )
                ],
                manufacturer="Generic",
                model="Dimmer 1 Channel"
            ),
            FixtureDefinition(
                parameter_definitions=[
                    FixtureParameterDefinition(
                        address=0,
                        default_value=0.0,
                        name="ColorRGB",
                        resolution=ParameterResolution.Simple,
                        type=ParameterType.ColorRGB
                    )
                ],
                manufacturer="Generic",
                model="Color RGB"
            )
        ]
    )

    generic_filepath =  JsonFixtureDefinitionStore.make_generic_libray_filepath()
    store = JsonFixtureDefinitionStore()
    store.set_library(library)
    store.save(generic_filepath)

    _logger.info("Test loading back")
    definition_store = JsonFixtureDefinitionStore()
    definition_store.load_default_library()

    for local_definition in library.definitions:
        assert local_definition == definition_store.get_by_identifier(local_definition.identifier)

    _logger.info("All definitions loaded back successfully")
