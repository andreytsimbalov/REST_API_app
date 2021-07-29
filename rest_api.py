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
def getPostCar():
    if request.method == 'POST':
        print('($1, $2)')
        json_f = request.get_json()
        print(json_f)
        return resp(200, db.car.insertOne(json_f))
        # return resp(200, {"cars": db.car.selectAll()})
    else:
        print("GET cars")
        return resp(200, {"cars": db.car.selectAll()})

@app.route('/cars/<int:cars_id>')
def getCarOne(cars_id):
    return resp(200, db.car.selectOne(cars_id))

if __name__ == '__main__':
    app.run()