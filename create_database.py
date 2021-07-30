# creates a database on a new device
# the device must have a mysql server

import mysql.connector as mysql_conn
import json


if __name__ == "__main__":
    with open('data/mysql_log_pas.json', 'r', encoding='utf-8') as f:
        sql_data = json.load(f)

    connection = mysql_conn.connect(
        user=sql_data['user'],
        password=sql_data['password'],
        host=sql_data['host'],
        port=sql_data['port']
    )
    cur = connection.cursor(buffered=True)
    print("Success connection to DB")

    try:
        cur.execute("CREATE DATABASE " + sql_data['database'])
        print("Success database", sql_data['database'], "created")
        connection.commit()
    except:
        print("Database", sql_data['database'], "was created earlier")
    connection.close()

    connection.connect(database=sql_data['database'])
    cur = connection.cursor(buffered=True)

    command = ''
    for line in open("data/dump-dealer_car-202107301235.sql"):
        if line=='\n':
            continue
        command+=line

        if command[-2] == ';':
            cur.execute(command)
            command = ''

    print("Success tables created")

