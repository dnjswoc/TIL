black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(user_list):
    censored_user_list = {}
    for i in range(len(user_list)):
        censored_user_list[user_list[i]['company']] = user_list[i]['name']
    black_list_bool = censorship(censored_user_list)
    censored_user_list = {}
    for i in range(len(user_list)):
        if black_list_bool[i] == True:
            censored_user_list[user_list[i]['company']] = [user_list[i]['name']]
    return censored_user_list



def censorship(censored_user_list):
    black_list_bool = []
    for key in censored_user_list.keys():
        if key in black_list:
            print(f'{key} 소속의 {str(censored_user_list[key])} 은/는 등록할 수 없습니다.')
            black_list_bool.append(False)
        else:
            print('이상 없습니다.')
            black_list_bool.append(True)
    return black_list_bool
    

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
create_user_list = create_user(dummy_data)
print(create_user_list)