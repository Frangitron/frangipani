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

    driver_infos = []
    for layer_name in ["Intermission", "Presentation", "Performance"]:
        driver_infos.extend([
            DriverInfo(
                name=layer_name + " Spots On",
                source_identifier=DriverSourceIdentifier(
                    control_address=f"{layer_name.lower()}_on"
                ),
                target_identifier=DriverTargetIdentifier(
                    layer_name=layer_name + " Spots",
                    targets_opacity=True
                ),
                fade_in_time = 1.0,
                fade_out_time = 1.0
            ),
            DriverInfo(
                name=layer_name + " Bowls Color",
                source_identifier=DriverSourceIdentifier(
                    control_address=f"{layer_name.lower()}_color"
                ),
                target_identifier=DriverTargetIdentifier(
                    layer_name=layer_name + " Bowls",
                    value_name="ColorRGB"
                ),
                fade_in_time=0.5,
                fade_out_time=0.5
            ),
            DriverInfo(
                name=layer_name + " Bowls On",
                source_identifier=DriverSourceIdentifier(
                    control_address=f"{layer_name.lower()}_on"
                ),
                target_identifier=DriverTargetIdentifier(
                    layer_name=layer_name + " Bowls",
                    targets_opacity=True
                ),
                fade_in_time=1.0,
                fade_out_time=1.0
            ),
        ])

    driver_infos.extend([
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
    ])

    pool = DriverPool(
        name="Demo Driver Pool",
        driver_infos=driver_infos
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
