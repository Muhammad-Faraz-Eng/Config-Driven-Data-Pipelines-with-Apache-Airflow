from typing import Dict, Type
from core.base.base_transformer import BaseTransformer
from core.transformations.identity_transformation import IdentityTransformation


class TransformationFactory:
    _registry: Dict[str, Type[BaseTransformer]] = {"identity": IdentityTransformation}

    @classmethod
    def register(
        cls, transformation_type: str, transformation_class: Type[BaseTransformer]
    ):
        if not issubclass(transformation_class, BaseTransformer):
            raise TypeError("Transformation class must inherit from BaseTransformation")
        cls._registry[transformation_type] = transformation_class

    @classmethod
    def create(cls, transformation_type: str, params: dict) -> BaseTransformer:
        if transformation_type not in cls._registry:
            raise ValueError(
                f"Transformation type not registered: {transformation_type}"
            )
        transformation_class = cls._registry[transformation_type]
        return transformation_class(params)
