import psycopg2
from sqlalchemy import create_engine
from core.base.base_connector import BaseConnector


class PostgresConnector(BaseConnector):
    def __init__(self, connection_config: dict):
        self.connection_config = connection_config
        self._conn = None

    def connect(self):
        if self._conn is None:
            self._conn = psycopg2.connect(
                user=self.connection_config["user"],
                password=self.connection_config["password"],
                host=self.connection_config["host"],
                port=int(self.connection_config["port"]),
                database=self.connection_config["database"],
            )
        return self._conn

    def close(self):
        if self._conn:
            self._conn.close()
            self._conn = None

    def get_engine(self):
        url = (
            f"postgresql+psycopg2://"
            f"{self.connection_config['user']}:"
            f"{self.connection_config['password']}@"
            f"{self.connection_config['host']}:"
            f"{self.connection_config['port']}/"
            f"{self.connection_config['database']}"
        )
        return create_engine(url)

    def execute(self, sql: str):
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                conn.commit()
