from core.base.base_target import BaseTarget
from core.connectors.postgres_connector import PostgresConnector
from core.config.connection_registry import ConnectionRegistry
import pandas as pd


class PostgresTarget(BaseTarget):
    def __init__(self, config: dict):
        super().__init__(config)
        self.connection_config = ConnectionRegistry.get(config["connection_id"])
        self.connector = PostgresConnector(self.connection_config)
        self.engine = None

    def connect(self):
        if self.engine is None:
            self.engine = self.connector.get_engine()

    def write(self, data: pd.DataFrame):
        schema = self.config["schema"]
        table = self.config["table"]
        mode = self.config.get("write_mode", "append")

        data.to_sql(
            name=table, schema=schema, con=self.engine, if_exists=mode, index=False
        )

    def close(self):
        self.connector.close()
