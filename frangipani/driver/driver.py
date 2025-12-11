from dataclasses import dataclass

from dataclasses_json import dataclass_json

from frangipani.driver.source_identifier import DriverSourceIdentifier
from frangipani.driver.target_identifier import DriverTargetIdentifier


@dataclass_json
@dataclass
class Driver:
    name: str
    target_identifier: DriverTargetIdentifier
    source_identifier: DriverSourceIdentifier

    source_value: float | bool | None = None
    enabled: bool = True
    fade_in_time: float = 0.0
    fade_out_time: float = 0.0
    inverted: bool = False
