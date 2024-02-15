from django.db import models
from django.contrib.auth.models import User



class Company(models.Model):
    name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE
                             , related_name='companies')  # companies that belong to a particular user
    about = models.TextField()

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self) -> str:
        return self.name