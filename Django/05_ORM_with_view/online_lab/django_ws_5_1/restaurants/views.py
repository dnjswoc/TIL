from django.shortcuts import render, redirect
from .models import Restaurants

# Create your views here.
def index(request):
    restaurants = Restaurants.objects.all()
    context = {
        'restaurants': restaurants,
    }
    return render(request, 'restaurants/index.html', context)


def new(request):
    return render(request, 'restaurants/new.html')


def create(request):
    restaurant = Restaurants()
    restaurant.name = request.POST.get('name')
    restaurant.description = request.POST.get('description')
    restaurant.address = request.POST.get('address')
    restaurant.phone_number = request.POST.get('phone_number')
    restaurant.save()
    return redirect('restaurants:index')