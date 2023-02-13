import requests

BASE_URL = 'https://motof.pythonanywhere.com/api'

data = {'name': 'Moto', 'age': 30}
r = requests.post(BASE_URL, json=data)

print(r.json())