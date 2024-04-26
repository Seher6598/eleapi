import cx_Oracle
from flask import Flask, request, jsonify
import datetime
import os
import dotenv
import json

dotenv.load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASS")

cx_Oracle.init_oracle_client(lib_dir=r"C:\app\client\30399\product\instantclient_19_12")

TNS = '''
 (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = crhcbsdb1.coruhedas.com.tr)(PORT = 1521))
      (ADDRESS = (PROTOCOL = TCP)(HOST = crhcbsdb2.coruhedas.com.tr)(PORT = 1521))
    )
    (CONNECT_DATA =
      (SERVICE_NAME = fedcbs)
    )
  )
'''



app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        with cx_Oracle.connect(USER, PASSWORD, TNS, encoding="UTF-8", nencoding="UTF-8") as conn:
            cur = conn.cursor()
            query = "SELECT assetid, update_date, type from ele_support_struct"
            result = cur.execute(query)
            row_headers = [x[0] for x in result.description]
            cur.rowfactory = lambda *args: dict(zip(row_headers, args))
            data = result.fetchall()
            data_list = [{key: value.isoformat() if isinstance(value, datetime.datetime) else value for key, value in
                          row.items()} for row in data]
            return jsonify(
                data=data_list,
                status="ok",
                msg="Veri sorgusu basarili"
            ), 200
    except Exception as ex:
            return jsonify(
                status="fail",
                msg=str(ex.args[0])
            ), 415











if __name__ == "__main__":
    app.run(debug=True)