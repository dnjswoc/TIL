from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.recommend, name='recommend'),
    path('bestseller/', views.bestseller, name='bestseller'),
]
