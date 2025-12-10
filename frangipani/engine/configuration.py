from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class EngineConfiguration:
    artnet_target_ip: str
    artnet_bind_address: str | None = None
    artnet_target_rate: int = 40
