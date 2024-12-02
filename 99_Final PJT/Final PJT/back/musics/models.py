from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='genres')


class Chart(models.Model):
    rank = models.IntegerField()
    track_id = models.CharField(max_length=255)
    artist_names = models.CharField(max_length=255)
    track_name = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    peak_rank = models.IntegerField()
    previous_rank = models.IntegerField()
    weeks_on_chart = models.IntegerField()
    streams = models.IntegerField()
    album_image = models.CharField(max_length=255)

