import cx_Oracle

class DB:
    def __init__(self, con_str, user, password):
        self.con_str = con_str
        self.user = user
        self.password = password
        self.connection = None

    def __enter__(self):
        try:
            conn = cx_Oracle.connect(self.user, self.password, self.con_str)
            self.connection = conn
            return self
        except Exception as err:
            print(f"veritabani baglantisi olusturulamadi: {err}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection is not None:
            self.connection.close()
    def query_db(self, sql):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                data = cursor.fetchall()
                column_names = [col[0] for col in cursor.description]

                result = []
                for row in data:
                    record_dict = dict(zip(column_names, row))
                    result.append(record_dict)
                return result
        except cx_Oracle.Error as err:
            print(f"Veritabani sorgusu hatasi: {err}")


