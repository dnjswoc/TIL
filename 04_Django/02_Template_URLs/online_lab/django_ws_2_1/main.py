import requests
from pprint import pprint

API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbdnjswoc1459005'
params = {
    'ttbkey': API_KEY,
    'QueryType': 'ItemNewSpecial',
    'SearchTarget': 'Book',
    'MaxResults': 50,
    'Output': 'JS',
    'Version': 20131101,
}

response = requests.get(API_URL, params= params)

response_json = response.json()

items = response_json.get('item')

answer = []

for item in items:
    answer.append({'국제 표준 도서 번호': item['isbn'],
                   '저자': item['author'],
                   '제목': item['title'],
                   '출간일': item['pubDate']})


pprint(answer)