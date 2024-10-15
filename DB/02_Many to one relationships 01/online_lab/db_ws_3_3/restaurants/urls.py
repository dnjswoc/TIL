from django.urls import path
from . import views


app_name = 'restaurants'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:restaurant_pk>/', views.detail, name='detail'),
    path('<int:pk>/menu/', views.menu_create, name='menu_create'),
]
