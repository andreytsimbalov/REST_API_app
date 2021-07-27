import requests

server_url = "https://my-json-server.typicode.com/typicode/demo/posts"

response = requests.get(server_url+"/1")

print(response)
print(response.json())

new_data = {
    'userId': 1,
    'id': 1,
    'title': 'qwe',
    'body': 'asd'
}

new_data = response.json()
response = requests.post(server_url+'/1', data = new_data)
print(response)
response = requests.get(server_url+"/1")
print(response.json())

