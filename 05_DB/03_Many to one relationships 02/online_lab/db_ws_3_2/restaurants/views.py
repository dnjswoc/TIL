from django.shortcuts import render, redirect
from .forms import RestaurantForm
from .models import Restaurant

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants,
    }
    return render(request, 'restaurants/index.html', context)


def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurants:index')
    else:
        form = RestaurantForm()
    context = {
        'form': form,
    }
    return render(request, 'restaurants/create.html', context)


def detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    context = {
        'restaurant': restaurant,
    }
    return render(request, 'restaurants/detail.html', context)