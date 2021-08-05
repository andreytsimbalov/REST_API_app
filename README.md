# REST_Api_app

REST API with support for CRUD operations.
The subject of this API is related to the sale of cars by car dealers.

## Installation guide

Required set of libraries:
- mysql-connector-python

Installation procedure:
1. Open **data/mysql_log_pas.json**, enter user data *MySql* server

		{
			"user": "user",
			"password": "password",
			"host":"localhost",
			"port":"3306",
			"database":"dealer_car"
		}
	
2. Run **create_database.py**


## User's manual

To start the server, you need to run **rest_api.py**

For one-time machine testing of all available operations *(GET, POST, PUT, DELETE)*, you need to run **test_requests.py** while the server is running

Supported methods *(for cars table, similar for dealers)*:

	GET     /cars
	GET     /cars/1
	POST    /cars
	PUT     /cars/1
	DELETE  /cars/1

Json examples for POST, PUT requests:

    car_json = {
      'dealer_id': 1,
      'name': 'car 1'
    }


    dealer_json = {
      'name': 'dealer 1'
    }
	
Request example:

    GET:  http://127.0.0.1:5000/dealers/3
    
    >> {"id": 3, "name": "Bob"}
