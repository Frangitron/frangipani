from dataclasses import dataclass
from typing import TypeVar, Generic

from dataclasses_json import dataclass_json


T = TypeVar('T')


@dataclass_json
@dataclass
class BaseLayerValue(Generic[T]):
    name: str
    parameter_selector: str
    value: T
