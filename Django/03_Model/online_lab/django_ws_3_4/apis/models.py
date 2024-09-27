from django.db import models

# Create your models here.
class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(max_length=200)
    documentation_url = models.URLField(max_length=200)
    auth_required = models.BooleanField()
    sample_data = models.JSONField(encoder=None, decoder=None)
    created_at = models.DateTimeField(auto_now_add=True)