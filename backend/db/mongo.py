from pymongo import MongoClient, errors
from typing import Optional

class MongoDB:
    _instance = None
    _client = None

    def __new__(cls, uri: Optional[str] = None):
        if cls._instance is None:
            cls._instance = super(MongoDB, cls).__new__(cls)
            try:
                db_name = uri.split('/')[-1]
                cls._client = MongoClient(uri, serverSelectionTimeoutMS=5000)
                # Trigger a server selection to check connection
                cls._client.server_info()
                cls._instance.db = cls._client[db_name]
                print('connection established')
            except errors.ServerSelectionTimeoutError as err:
                print(f"Could not connect to MongoDB: {err}")
                cls._instance.db = None
        return cls._instance

    def get_collection(self, name):
        if self.db is None:
            raise ConnectionError("No MongoDB connection available.")
        return self.db[name]

    def close(self):
        if self._client:
            self._client.close()
            self._client = None
            self.db = None
            MongoDB._instance = None
