from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from frangipani.driver.driver_info import DriverInfo


@dataclass_json
@dataclass
class DriverPoolStorable:
    name: str
    driver_infos: list[DriverInfo] = field(default_factory=list)
