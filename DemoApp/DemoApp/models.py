import imp
from urllib.parse import MAX_CACHE_SIZE
from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 20)
    pwd = models.CharField(max_length = 16)
    name = models.CharField(max_length = 30)
    contact_no = models.CharField(max_length = 14)
    gender = models.CharField(max_length = 1)
    address = models.CharField(max_length = 100)