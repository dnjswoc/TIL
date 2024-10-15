from django import forms
from .models import Restaurant, Menu


class RestaurantForm(forms.ModelForm):
    
    class Meta:
        model = Restaurant
        fields = '__all__'

class MenuForm(forms.ModelForm):
    
    class Meta:
        model = Menu
        exclude = ('restaurant', )


class MenuChangeForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('price', 'is_vegan',)