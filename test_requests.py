import requests
import random as r

url = "http://127.0.0.1:5000"
url_cars = "http://127.0.0.1:5000/cars"
url_dealers = "http://127.0.0.1:5000/dealers"

car_json = {
    'dealer_id': r.randint(1, 5),
    'name': 'car i_' + str(r.randint(0, 100))
}

dealer_json = {
    'name': 'dealer i_' + str(r.randint(0, 100))
}

def printResponses(response):
    print(response)
    print(response.json())
    print()

if __name__ == "__main__":
    print("Start test requests to CARS")
    print()

    print("GET all")
    printResponses(requests.get(url_cars))

    # response = requests.post(url_cars, json = car_json)

    # response = requests.get(url_cars+'/1')
    # response = requests.put(url_cars+'/9', json = car_json)
    # response = requests.delete(url_cars+'/10')



    # response = requests.get(url_dealers)
    # response = requests.post(url_dealers, json = dealer_json)
    #
    # response = requests.get(url_dealers+'/1')
    # response = requests.put(url_dealers+'/19', json = dealer_json)
    # response = requests.delete(url_dealers+'/19')

    # print(response)
    # print(response)
    # print(response.json())
    # print()

