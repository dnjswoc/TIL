import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'
dummy_data = []
for i in range(10):
    new_url = API_URL + str(i+1)
    response = requests.get(new_url)
    parsed_data = response.json()
    dummy_data.append(parsed_data['name'])        
print(dummy_data)
