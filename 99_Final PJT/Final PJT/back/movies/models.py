from django.db import models
from django.conf import settings


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    overview = models.CharField(max_length=255)
    release_date =models.DateField()
    runtime = models.IntegerField()
    vote_average = models.FloatField()
    poster_path = models.CharField(max_length=255)
    genre1 = models.CharField(max_length=50, blank=True)
    genre2 = models.CharField(max_length=50, blank=True)
    genre3 = models.CharField(max_length=50, blank=True)
    actor1 = models.CharField(max_length=50, blank=True)
    actor2 = models.CharField(max_length=50, blank=True)
    actor3 = models.CharField(max_length=50, blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movies')


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MovieGenre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
