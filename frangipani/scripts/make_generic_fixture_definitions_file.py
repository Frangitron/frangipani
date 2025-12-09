import logging
import os

from pyside6helpers import resources

from frangipani.fixture_definition import (
    FixtureDefinition,
    FixtureDefinitionLibrary,
    FixtureDefinitionStore,
    ParameterDefinition,
    ParameterResolutionEnum,
    ParameterTypeEnum,
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
                    ParameterDefinition(
                        address=0,
                        default_value=0.0,
                        name="Dimmer",
                        resolution=ParameterResolutionEnum.Simple,
                        type=ParameterTypeEnum.Dimmer
                    )
                ],
                manufacturer="Generic",
                model="Dimmer 1 Channel"
            ),
            FixtureDefinition(
                parameter_definitions=[
                    ParameterDefinition(
                        address=0,
                        default_value=0.0,
                        name="Dimmer",
                        resolution=ParameterResolutionEnum.Simple,
                        type=ParameterTypeEnum.ColorRGB
                    )
                ],
                manufacturer="Generic",
                model="Color RGB"
            )
        ]
    )

    generic_filepath = resources.find(os.path.join("fixture_definition_libraries", "generic.json"))
    FixtureDefinitionStore().save(library, generic_filepath)

    _logger.info("Test loading back")
    loaded_library = FixtureDefinitionStore.load_library_file(generic_filepath)

    for local_definition, loaded_definition in zip(library.definitions, loaded_library.definitions):
        assert local_definition == loaded_definition

    _logger.info("All definitions loaded back successfully")
