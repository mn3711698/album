from __future__ import unicode_literals

from django.db import models

# Create your models here.
class tests(models.Model):
    time  = models.CharField(max_length=255)
    hotelname  = models.CharField(max_length=255)
    accounts  = models.CharField(max_length=255)
    mintor_data  = models.CharField(max_length=255)
    url  = models.CharField(max_length=255)
    timestamp  = models.CharField(max_length=255)
