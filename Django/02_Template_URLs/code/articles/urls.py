from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name="index"),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.greeting, name='detail'),
    path('articles/<int:num>/', views.detail, name='greeting'),
]
