import requests
import random as r

url = "http://127.0.0.1:5000"
url_cars = "http://127.0.0.1:5000/cars"
url_dealers = "http://127.0.0.1:5000/dealers"

car_json = {
    'dealer_id': r.randint(1, 4),
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
    # Start test requests to CARS
    print("Start test requests to CARS")
    print()

    print("test GET all")
    printResponses(requests.get(url_cars))

    print("test POST one")
    printResponses(requests.post(url_cars, json=car_json))

    last_post_id = requests.get(url_cars).json()['cars'][-1]['id']
    print("Last POST id:", last_post_id)
    print()

    print("test GET one")
    printResponses(requests.get(url_cars + '/' + str(last_post_id)))

    print("test PUT one")
    printResponses(requests.put(url_cars + '/' + str(last_post_id), json=car_json))

    print("test DELETE one")
    printResponses(response=requests.delete(url_cars + '/' + str(last_post_id)))

    # Start test requests to DEALERS
    print()
    print("Start test requests to DEALERS")
    print()

    print("test GET all")
    printResponses(requests.get(url_dealers))

    print("test POST one")
    printResponses(requests.post(url_dealers, json=dealer_json))

    last_post_id = requests.get(url_dealers).json()['cars'][-1]['id']
    print("Last POST id:", last_post_id)
    print()

    print("test GET one")
    printResponses(requests.get(url_dealers + '/' + str(last_post_id)))

    print("test PUT one")
    printResponses(requests.put(url_dealers + '/' + str(last_post_id), json=dealer_json))

    print("test DELETE one")
    printResponses(requests.delete(url_dealers + '/' + str(last_post_id)))
