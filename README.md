# REST_Api_app

REST API с поддержкой CRUD операций.
Тематика данного API связана с продажами машин автодилерами.

## Руководство по установке

Необходимый набор библиотек:
- mysql-connector-python

Порядок установки:
1. Открыть **data/mysql_log_pas.json**, ввести данные пользователя *MySql* сервера

		{
			"user": "user",
			"password": "password",
			"host":"localhost",
			"port":"3306",
			"database":"dealer_car"
		}
	
2. Запустить **create_database.py**


## Руководство пользователя

Для старта сервера необходимо запустить **rest_api.py**

Для тестирования всех доступных операций *(GET, POST, PUT, DELETE)* неоходимо запустить **test_requests.py**
	
Поддериваемые методы *(для таблицы cars, аналогично для dealers)*:

	GET     /cars
	GET     /cars/1
	POST    /cars
	PUT     /cars/1
	DELETE  /cars/1

Примеры Json для POST, PUT запросов:

    car_json = {
      'dealer_id': 1,
      'name': 'car 1'
    }


    dealer_json = {
      'name': 'dealer 1'
    }
	
Пример запроса:

    GET:  http://127.0.0.1:5000/dealers/3
    
    >> {"id": 3, "name": "Bob"}
