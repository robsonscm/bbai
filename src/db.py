import json
import os

import mysql.connector


class DbConnector:
    def __init__(self):
        self.err = None
        self.cnx = None
        with open(os.path.abspath(".db_config.json")) as f:
            self.config = json.load(f)

        self.cnx = mysql.connector.connect(**self.config)

    def execute(self, query):
        data = None
        cursor = self.cnx.cursor(dictionary=True)
        rows_count = cursor.execute(query)
        if cursor.description is not None:
            data = cursor.fetchall()
        cursor.close()
        return data
