from typing import List, Iterable, Any

from core.base.base_source import BaseSource
from core.base.base_target import BaseTarget
from core.base.base_transformer import BaseTransformer


class BasePipeline:
    def __init__(
        self,
        source: BaseSource,
        transformations: List[BaseTransformer],
        target: BaseTarget,
    ):
        self.source = source
        self.transformations = transformations
        self.target = target

    def run(self) -> None:
        try:
            self.source.connect()
            self.target.connect()

            records = self.source.read()

            records = self._apply_transformation(records)

            self.target.write(records)
        finally:
            self.source.close()
            self.target.close()

    def _apply_transformation(self, records: Iterable[Any]) -> Iterable[Any]:
        for transformation in self.transformations:
            records = transformation.transform(records)
        return records
