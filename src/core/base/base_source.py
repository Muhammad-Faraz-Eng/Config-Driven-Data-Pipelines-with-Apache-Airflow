from abc import ABC, abstractmethod
from typing import Iterable, Any


class BaseSource(ABC):
    def __init__(self, config: dict):
        self.config = config

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def read(self) -> Iterable[Any]:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
