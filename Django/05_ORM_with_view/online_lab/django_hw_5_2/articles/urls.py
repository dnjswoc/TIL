from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.main, name='main'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
