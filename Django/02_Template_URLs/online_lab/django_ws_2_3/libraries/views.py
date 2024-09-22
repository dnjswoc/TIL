from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')


def recommend(request):
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

    book_list = []

    for dict in answer:
        book_list.append([dict['제목'], dict['저자']])

    context = {
        'book_list': book_list,
    }
    return render(request, 'recommend.html', context)