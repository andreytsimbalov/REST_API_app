import mysql.connector as mysql_conn
import json

# CREATE TABLE dealer_car.dealer (
# # 	id INT auto_increment NOT NULL,
# # 	name varchar(100) NULL,
# # 	CONSTRAINT dealer_pk PRIMARY KEY (id)
# # )

# CREATE TABLE dealer_car.car (
# 	id INT auto_increment NOT NULL,
# 	dealer_id INT NOT NULL,
# 	name varchar(100) NULL,
# 	CONSTRAINT car_pk PRIMARY KEY (id),
# 	CONSTRAINT car_FK FOREIGN KEY (dealer_id) REFERENCES dealer_car.dealer(id)
# )

class Database():
    def __init__(self):
        with open('mysql_log_pas.json', 'r', encoding='utf-8') as f:
            self.sql_data = json.load(f)
        self.connection = mysql_conn.connect(
            user=self.sql_data['user'],
            password=self.sql_data['password'],
            host=self.sql_data['host'],
            port=self.sql_data['port'],
            database=self.sql_data['database']
        )
        self.cur = self.connection.cursor(buffered=True)

        self.dealer = Dealer(self.connection)
        self.car = Car(self.connection)


class Car():
    def __init__(self, db_connection):
        self.connection = db_connection
        self.cur = self.connection.cursor(buffered=True)


    def selectAll(self):
        self.cur.execute("SELECT id, dealer_id, name FROM car")
        tuples = self.cur.fetchall()
        dealers = []
        for (id, dealer_id, name) in tuples:
            dealers.append({"id": id, 'dealer_id': dealer_id, "name": name})
        return dealers

    def selectOne(self, id):
        self.cur.execute("SELECT id, dealer_id, name FROM car WHERE id = %s" % (id))
        tuples = self.cur.fetchone()
        if tuples == None:
            dealers = {}
        else:
            dealers = {"id": tuples[0], 'dealer_id': tuples[1], "name": tuples[2]}
        return dealers

    def insertOne(self, json_data):
        self.cur.execute("INSERT INTO car (dealer_id, name) VALUES (%s, %s)",
                         (json_data['dealer_id'], json_data['name']))
        self.cur.execute("SELECT LAST_INSERT_ID()")
        self.connection.commit()
        tuples = self.selectOne(self.cur.fetchone()[0])
        return tuples

    def updateOne(self, json_data, id):
        self.cur.execute("UPDATE car SET dealer_id = %s, name = %s WHERE id = %s",
                         (json_data['dealer_id'], json_data['name'], id))
        self.connection.commit()
        tuples = self.selectOne(id)
        return tuples

    def deleteOne(self, id):
        self.cur.execute("DELETE FROM car WHERE id = %s" % (id))
        self.connection.commit()
        tuples = self.selectOne(id)
        return tuples



class Dealer():
    def __init__(self, db_connection):
        self.connection = db_connection
        self.cur = self.connection.cursor(buffered=True)


    def selectAll(self):
        self.cur.execute("SELECT id, name FROM dealer")
        tuples = self.cur.fetchall()
        dealers = []
        for (id, name) in tuples:
            dealers.append({"id": id, "name": name})
        return dealers

    def selectOne(self, id):
        self.cur.execute("SELECT id, name FROM dealer WHERE id = %s" % (id))
        tuples = self.cur.fetchone()
        if tuples == None:
            dealers = {}
        else:
            dealers = {"id": tuples[0], "name": tuples[1]}
        return dealers

    def insertOne(self, json_data):
        self.cur.execute("INSERT INTO dealer (name) VALUES ('"+json_data['name']+"')")
        self.cur.execute("SELECT LAST_INSERT_ID()")
        self.connection.commit()
        tuples = self.selectOne(self.cur.fetchone()[0])
        return tuples

    def updateOne(self, json_data, id):
        self.cur.execute("UPDATE dealer SET name = %s WHERE id = %s", (json_data['name'], id))
        self.connection.commit()
        tuples = self.selectOne(id)
        return tuples

    def deleteOne(self, id):
        self.cur.execute("DELETE FROM dealer WHERE id = %s" % (id))
        self.connection.commit()
        tuples = self.selectOne(id)
        return tuples


if __name__ == "__main__":
    db = Database()
    # db.cur.execute("show tables")
    # db.cur.execute("SELECT * FROM dealer")
    # db.cur.execute("INSERT INTO dealer (name) VALUES ('') RETURNING id" % (json_data['name']))
    for i in db.dealer.selectAll():
        print(i)

    for i in db.car.selectAll():
        print(i)

    print()
    json_data = {
        'dealer_id' : 5,
        'name': 'car i'
    }
    db.car.insertOne(json_data)
    # db.car.insertOne(json_data)
    # db.car.updateOne(json_data, 6)
    # db.car.deleteOne(6)

    for i in db.car.selectAll():
        print(i)