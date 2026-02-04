from abc import ABC, abstractmethod
from typing import Iterable, Any


class BaseTarget(ABC):
    def __init__(self, config: dict):
        self.config = config

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def write(self, records: Iterable[Any]) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
