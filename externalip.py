import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

response = urlopen(url)

data = json.load(response)

ip = data['ip']
org = data['org']
city = data['city']
region = data['region']

print('detalhes do seu ip externo:')
print(f"ip: {data['ip']}")
print(f"org: {data['org']}")
print(f"city: {data['city']}")
print(f"city: {data['region']}")