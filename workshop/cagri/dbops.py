
import cx_Oracle

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
            return self.connection
        except Exception as ex:
            print(f"Veri tabani baglantisi olusturulamadi: {ex}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection is not None:
            self.connection.close()


    def query_db(self, sql, sql_params):

        '''
        veri tabanından sorgu çekerek sorgu sonucunu json objelerden oluşan bir array olarak döndürür

        :param sql:
        :param sql_params:
        :return:
        '''
        pass

