from django.db import models
import requests
from pprint import pprint

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()

    @classmethod
    def insert_data(cls):
        API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
        API_KEY = 'ttbdnjswoc1459005'
        params = {
            'ttbkey': API_KEY,
            'QueryType': 'ItemNewAll',
            'SearchTarget': 'Book',
            'MaxResults': 10,
            'Output': 'JS',
            'Version': 20131101,
        }

        response = requests.get(API_URL, params= params)
        
        data = response.json().get('item')
        # pprint(data)
        for item in data:
            my_model = cls(isbn=item['isbn'], author=item['author'], title=item['title'], category_name=item['categoryName'],
                           category_id=item['categoryId'], price=item['priceStandard'], fixed_price=item['fixedPrice'], pub_date=item['pubDate'])
            my_model.save()
