from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    genre1 = models.CharField(max_length=50, blank=True)
    genre2 = models.CharField(max_length=50, blank=True)
    introduction = models.TextField(blank=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')