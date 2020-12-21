from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class mylist(models.Model):
    name=models.CharField(max_length=200)
    time = models.CharField(blank=True, null=True, max_length=50)
    username33 = models.CharField(blank=True, null=True, max_length=50)

    def __str__(self):
        return self.name


