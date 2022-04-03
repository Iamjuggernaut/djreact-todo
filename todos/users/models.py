from django.db import models
from uuid import uuid4


class User(models.Model):
    uid = models.UUIDField()
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=254)