from flask import Flask, jsonify
from flask import request
import psycopg2

# Credentials for Postgresql
host = "************************************************"
database = "dbname"
user = "username"
password = "***********"
port = "5432"

app = Flask(__name__)


@app.route("/listdetails", methods=['GET', 'POST'])
def geneva_get():
    failed_status = {"status": "failed"}
    try:
        con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        cursor = con.cursor()
        cursor.execute("select * from public.patient")
        result = cursor.fetchall()
        return jsonify(result)    
    except psycopg2.OperationalError as e:
        failed_status["error"] = str(e)
        return jsonify(failed_status)

if __name__ == '__main__':
    app.run(debug=True)
