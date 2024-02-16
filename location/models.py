from django.db import models
from django.contrib.auth.models import User



class Location(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)