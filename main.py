from workshop.gurkan.dbops import DBOps
import dotenv
import os
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir = r"C:\App\instantclient_21_6")
dotenv.load_dotenv()

USER =os.getenv("DBUSER")
PASSWORD = os.getenv("DBPASS")

TNS = '''
  (DESCRIPTION =
    (ADDRESS_LIST =
        (FAILOVER = ON)
      (LOAD_BALANCE = yes)  
      (ADDRESS = (PROTOCOL = TCP)(HOST = 172.30.3.102)(PORT = 1521))
      (ADDRESS = (PROTOCOL = TCP)(HOST = 172.30.3.103)(PORT = 1521))
    )
    (CONNECT_DATA =
      (SERVICE_NAME = gis)
    )
  )
'''
sql = "SELECT * FROM ab_sube_il_ilce where sirketid = :1"
sql_params = (2,)


def gurkan_sample():
    with DBOps(tns_desc=TNS, user=USER, pwd=PASSWORD) as db:
        results_json = db.query_db(sql, sql_params)
        print(results_json)



if __name__=="__main__":
    gurkan_sample()