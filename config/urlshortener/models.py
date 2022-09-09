from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=500)
    shortened = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    #author