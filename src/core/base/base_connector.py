from abc import ABC, abstractmethod


class BaseConnector(ABC):
    def __init__(self, connection_id: str):
        self.connection_id = connection_id
        self._connection = None

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @property
    def connection(self):
        if self._connection is None:
            self._connection = self.connect()
        return self._connection
