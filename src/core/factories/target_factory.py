from typing import Type
from core.base.base_target import BaseTarget
from core.targets.postgres_target import PostgresTarget

class TargetFactory:
    _registry: dict[str, Type[BaseTarget]] = {
        'postgres': PostgresTarget
    }

    @classmethod
    def register(cls, target_type: str, target_class: Type[BaseTarget]) -> None:
        cls._registry[target_type] = target_class

    @classmethod
    def create(cls, target_type: str, config: dict) -> BaseTarget:
        if target_type not in cls._registry:
            raise ValueError(f"Target Type not register: {target_type}")
        return cls._registry[target_type](config)
