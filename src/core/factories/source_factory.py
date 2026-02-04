from typing import Type
from core.base.base_source import BaseSource
from core.sources.postgres_source import PostgresSource

class SourceFactory:
    _registry: dict[str, Type[BaseSource]] = {
        'postgres': PostgresSource
    }

    @classmethod
    def register(cls, source_type: str, source_class: Type[BaseSource]) -> None:
        cls._registry[source_type] = source_class

    @classmethod
    def create(cls, source_type: str, config: dict) -> BaseSource:
        if source_type not in cls._registry:
            raise ValueError(f"Source type not registered: {source_type}")
        return cls._registry[source_type](config)
