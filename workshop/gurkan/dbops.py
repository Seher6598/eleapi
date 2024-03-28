import cx_Oracle
import json

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
            print(f"Veritabani baglantisi hatasi: {ex}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection is not None:
            self.connection.close()

    def query_db(self, sql, sql_params):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, sql_params)
                columns = [col[0] for col in cursor.description]
                results = [dict(zip(columns, row)) for row in cursor.fetchall()]
                return json.dumps(results, ensure_ascii=False)
        except Exception as ex:
            print(f"Veritabani sorgu hatasi: {ex}")



