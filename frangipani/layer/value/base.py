from abc import abstractmethod, ABC

from dataclasses import dataclass
from typing import TypeVar, Generic

from dataclasses_json import dataclass_json, config


T = TypeVar("T")


@dataclass_json
@dataclass
class BaseLayerValue(ABC, Generic[T]):
    name: str
    parameter_selector: str
    value: T

    @abstractmethod
    def set_value_from_channels(self, channel_values: tuple[float, ...]) -> None:
        pass

    def __str__(self) -> str:
        return f"<{self.__class__.__name__}('{self.name}')>"
