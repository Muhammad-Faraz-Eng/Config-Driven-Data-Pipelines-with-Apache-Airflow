import pandas as pd
from core.base.base_source import BaseSource
from core.connectors.postgres_connector import PostgresConnector
from core.config.connection_registry import ConnectionRegistry


class PostgresSource(BaseSource):
    def __init__(self, config: dict):
        super().__init__(config)
        connection_config = ConnectionRegistry.get(config["connection_id"])
        self.connector = PostgresConnector(connection_config)
        self.engine = None

    def connect(self):
        if self.engine is None:
            self.engine = self.connector.get_engine()

    def read(self):
        self.connect()
        schema = self.config["schema"]
        table = self.config["table"]

        query = f"SELECT * FROM {schema}.{table}"
        engine = self.connector.get_engine()

        return pd.read_sql(query, engine)

    def close(self):
        self.connector.close()
        self.engine = None
