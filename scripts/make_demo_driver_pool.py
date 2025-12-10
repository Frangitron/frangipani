import logging

from frangipani.driver import (
    Driver,
    DriverPool,
    DriverSourceIdentifier,
    DriverTargetIdentifier,
    JsonDriverPoolStore,
)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    _logger = logging.getLogger("Script:MakeDemoDriverPool")

    pool = DriverPool(
        name="Demo Driver Pool",
        drivers=[
            Driver(
                name="DimmerFixture (all parameters)",
                source=DriverSourceIdentifier(
                    control_address="dimmer_fixtures_all_parameters"
                ),
                target=DriverTargetIdentifier(
                    layer_name="DimmerFixtures all parameters",
                    value_name="All",
                ),
            ),
            Driver(
                name="Blackout",
                source=DriverSourceIdentifier(
                    control_address="master_dimmer"
                ),
                target=DriverTargetIdentifier(
                    layer_name="Blackout",
                    targets_opacity=True
                ),
                inverted=True,
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
        assert driver == store.get_by_name(driver.name)
