# https://flask-russian-docs.readthedocs.io/ru/latest/quickstart.html

from flask import Flask, Response, request
from crud_tables import *
app = Flask(__name__)
db = Database()

def to_json(data):
    return json.dumps(data) + "\n"

def resp(code, data):
    return Response(
        status=code,
        mimetype="application/json",
        response=to_json(data)
    )

@app.route('/')
def hello_world():
    return 'REST API'

@app.route('/cars', methods=['POST', 'GET'])
def carGetPost():
    if request.method == 'POST':
        json_f = request.get_json()
        print("POST cars", json_f)
        return resp(200, db.car.insertOne(json_f))
    elif request.method == 'GET':
        print("GET cars")
        return resp(200, {"cars": db.car.selectAll()})

@app.route('/cars/<int:cars_id>', methods=['PUT', 'GET', 'DELETE'])
def carOneGetPutDelete(cars_id):
    if request.method == 'GET':
        print("GET car", cars_id)
        return resp(200, db.car.selectOne(cars_id))
    elif request.method == 'PUT':
        json_f = request.get_json()
        print("PUT car", cars_id, json_f)
        return resp(200, db.car.updateOne(json_f, cars_id))
    elif request.method == 'DELETE':
        print("DELETE car", cars_id)
        return resp(200, db.car.deleteOne(cars_id))



@app.route('/dealers', methods=['POST', 'GET'])
def dealerGetPost():
    if request.method == 'POST':
        json_f = request.get_json()
        print("POST dealers", json_f)
        return resp(200, db.dealer.insertOne(json_f))
    elif request.method == 'GET':
        print("GET dealers")
        return resp(200, {"dealers": db.dealer.selectAll()})

@app.route('/dealers/<int:dealers_id>', methods=['PUT', 'GET', 'DELETE'])
def dealerOneGetPutDelete(dealers_id):
    if request.method == 'GET':
        print("GET dealer", dealers_id)
        return resp(200, db.dealer.selectOne(dealers_id))
    elif request.method == 'PUT':
        json_f = request.get_json()
        print("PUT dealer", dealers_id, json_f)
        return resp(200, db.dealer.updateOne(json_f, dealers_id))
    elif request.method == 'DELETE':
        print("DELETE dealer", dealers_id)
        return resp(200, db.dealer.deleteOne(dealers_id))


if __name__ == '__main__':
    app.run()