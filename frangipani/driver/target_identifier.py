from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class DriverTargetIdentifier:
    layer_name: str
    value_name: str | None = None
    targets_opacity: bool | None = None

    def __post_init__(self):
        if self.targets_opacity is None and self.value_name is None:
            raise ValueError("Either layer_opacity or value_name must be set")

        if self.targets_opacity is not None and self.value_name is not None:
            raise ValueError("Only one of layer_opacity or value_name can be set")
