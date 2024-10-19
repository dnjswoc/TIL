from django import forms
from .models import Movie, Comment

class CreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ('title', 'description',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )