from yunusEmre.dbops import DB
import cx_Oracle
from dotenv import load_dotenv
import os
def tablo_veri():
    try:
        load_dotenv()
        USER = os.getenv("DB_USER")
        PASSWORD = os.getenv("DB_PASS")

        with DB("(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=frtcbsdb1.firatedas.com.tr)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=cedcbs)))", USER, PASSWORD) as db:
            if db is not None:
                result = db.query_db("select * from trabzon061.city_spatial")
                return result
    except Exception as e:
        print(f"Hata olustu: {e}")

if __name__ == "__main__":
    result = tablo_veri()
    print(result)
