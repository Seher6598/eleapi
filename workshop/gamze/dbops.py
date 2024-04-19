import cx_Oracle
import json
from datetime import datetime

class DBOps:
    def __init__(self, tns_desc, user, pwd):
        self.tns_desc = tns_desc
        self.user = user
        self.password = pwd
        self.connection = None

    def __enter__(self):
        try:
            conn = cx_Oracle.connect(self.user, self.password, self.tns_desc)
            self.connection = conn
            return self
        except Exception as ex:
            print(f"Bağlantı oluşturulamadı: {ex}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection is not None:
            self.connection.close()

    def query_db(self, sql, sql_params):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, sql_params)
            rows = cursor.fetchall()

            result = []
            for row in rows:
                formatted_row = {}
                for index, value in enumerate(row):
                    column_name = cursor.description[index][0]
                    if isinstance(value, datetime):
                        formatted_row[column_name] = value.strftime(
                            "%d/%m/%Y %H:%M:%S")
                    else:
                        formatted_row[column_name] = value
                result.append(formatted_row)

        return json.dumps(result)






















































































