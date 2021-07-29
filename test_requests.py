import requests
import random as r
import json

url = "http://127.0.0.1:5000"
url_cars = "http://127.0.0.1:5000/cars"
# url = "http://127.0.0.1:5000"

car_json = {
    'dealer_id': r.randint(1, 5),
    'name': 'car i_' + str(r.randint(0, 100))
}

# response = requests.get(url_cars)
# print(response)
# print(response.json())

# response = requests.post(url_cars, json = json.dumps(car_json))
response = requests.post(url_cars, json = car_json)

print(response)
print(response.json())
