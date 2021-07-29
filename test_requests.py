import requests
import random as r
import json

url = "http://127.0.0.1:5000"
url_cars = "http://127.0.0.1:5000/cars"
url_dealers = "http://127.0.0.1:5000/dealers"

car_json = {
    'dealer_id': r.randint(1, 5),
    'name': 'car i_' + str(r.randint(0, 100))
}

# response = requests.get(url_cars)
# print(response)
# print(response.json())

# response = requests.get(url_cars)
# response = requests.post(url_cars, json = car_json)

# response = requests.get(url_cars+'/1')
# response = requests.put(url_cars+'/9', json = car_json)
# response = requests.delete(url_cars+'/10')


dealer_json = {
    'name': 'dealer i_' + str(r.randint(0, 100))
}

# response = requests.get(url_dealers)
# response = requests.post(url_dealers, json = dealer_json)
#
# response = requests.get(url_dealers+'/1')
# response = requests.put(url_dealers+'/19', json = dealer_json)
response = requests.delete(url_dealers+'/19')


print(response)
print(response.json())
