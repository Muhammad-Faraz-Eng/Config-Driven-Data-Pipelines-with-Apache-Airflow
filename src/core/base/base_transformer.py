from abc import ABC, abstractmethod
from typing import Iterable, Any


class BaseTransformer(ABC):
    @abstractmethod
    def transform(self, records: Iterable[Any]) -> Iterable[Any]:
        pass
