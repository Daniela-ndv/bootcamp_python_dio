import requests

request = requests.get('http://127.0.0.1:8000/')
#request = requests.get('http://127.0.0.1:8000/random')
#request = requests.get('http://127.0.0.1:8000/random/30')

print(request.json())



