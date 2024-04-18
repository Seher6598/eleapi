""
from workshop.cagri.dbops import DBOps
from dotenv import load_dotenv
load_dotenv()
import os

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASS")

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



def cagri_sample():


    with DBOps(tns_desc=TNS, user=USER, pwd=PASSWORD) as db:
        db.query_db()







if __name__=="__main__":
    pass