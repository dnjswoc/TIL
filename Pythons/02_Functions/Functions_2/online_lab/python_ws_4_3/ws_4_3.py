import requests
from pprint import pprint as print


# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/1'


dummy_data = []
for i in range(10):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{i+1}')
    parsed_data = response.json()
    if float(parsed_data['address']['geo']['lat']) < 80 and float(parsed_data['address']['geo']['lng']) > -80:
        dummy_data.append({'company' : parsed_data['company']['name'], 'lat' : parsed_data['address']['geo']['lat'], 'lng' : parsed_data['address']['geo']['lng'], 'name' : parsed_data['name']})
print(dummy_data)

