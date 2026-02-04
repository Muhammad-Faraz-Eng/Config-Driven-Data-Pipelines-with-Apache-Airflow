from core.base.base_transformer import BaseTransformer


class IdentityTransformation(BaseTransformer):
    def __init__(self, params: dict | None = None):
        self.params = params or {}

    def transform(self, data):
        return data
