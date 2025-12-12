import logging

from pythonhelpers.injector import Injector

from frangipani.driver import (
    DriverInfo,
    DriverPool,
    DriverSourceIdentifier,
    DriverTargetIdentifier,
    JsonDriverPoolStore,
)
from frangipani.fixture.parameter.channel.channel_kind import (
    FixtureParameterChannelKind,
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
                name="Spots Dimmer",
                source_identifier=DriverSourceIdentifier(
                    control_address="spot_dimmer"
                ),
                target_identifier=DriverTargetIdentifier(
                    layer_name="Spots",
                    value_name="Dimmer",
                ),
            ),
            DriverInfo(
                name="RGB Dimmer",
                source_identifier=DriverSourceIdentifier(
                    control_address="rgb_dimmer"
                ),
                target_identifier=DriverTargetIdentifier(
                    layer_name="RGB",
                    value_name="Dimmer",
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
                fade_in_time=0.5,
                fade_out_time=0.5,
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
