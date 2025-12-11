import logging

from pythonhelpers.injector import Injector

from frangipani.driver import (
    DriverInfo,
    DriverPool,
    DriverSourceIdentifier,
    DriverTargetIdentifier,
    JsonDriverPoolStore,
)
from frangipani.time_provider import (
    ITimeProvider,
    TimeProvider,
)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    _logger = logging.getLogger("Script:MakeDemoDriverPool")

    Injector().set_dependencies({
        ITimeProvider: TimeProvider(),
    })

    pool = DriverPool(
        name="Demo Driver Pool",
        driver_infos=[
            DriverInfo(
                name="DimmerFixture (all parameters)",
                source_identifier=DriverSourceIdentifier(
                    control_address="dimmer_fixtures_all_parameters"
                ),
                target_identifier=DriverTargetIdentifier(
                    layer_name="DimmerFixtures all parameters",
                    value_name="All",
                ),
            ),
            DriverInfo(
                name="Master Dimmer",
                source_identifier=DriverSourceIdentifier(
                    control_address="master_dimmer"
                ),
                target_identifier=DriverTargetIdentifier(
                    layer_name="Master Dimmer",
                    targets_opacity=True
                ),
                inverted=True,
            ),
            DriverInfo(
                name="Blackout",
                source_identifier=DriverSourceIdentifier(
                    control_address="blackout"
                ),
                target_identifier=DriverTargetIdentifier(
                    layer_name="Blackout",
                    targets_opacity=True,
                ),
                fade_in_time=1.0,
                fade_out_time=1.0,
            )
        ]
    )

    store = JsonDriverPoolStore()
    store.set_pool(pool)
    store.save("demo.drivers.json")

    #
    # Test loading back
    store = JsonDriverPoolStore()
    store.load("demo.drivers.json")
    for driver in pool.drivers:
        assert driver.info.name == store.get_by_name(driver.info.name).info.name
