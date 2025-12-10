from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from frangipani.driver.driver import Driver


@dataclass_json
@dataclass
class DriverPool:
    name: str
    drivers: list[Driver] = field(default_factory=list)

    # Todo : raise on duplicate driver name
