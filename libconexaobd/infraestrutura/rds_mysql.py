# database_connector/adapters/rds_adapter.py

import pymysql
from .interfaces import DatabaseAdapter

class RDSAdapter(DatabaseAdapter):
    def __init__(self, host, port, dbname, user, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password

    def connect(self):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.dbname
        )

    def execute_query(self, query: str):
        conn = self.connect()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
        finally:
            conn.close()
        return result
