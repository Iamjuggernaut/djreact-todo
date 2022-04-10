from django.db import models
from uuid import uuid4


class User(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=254)
    


class Project(models.Model):
    name = models.CharField(max_length=150)
    users = models.ManyToManyField(User)


class Todo(models.Model):
    text = models.CharField(max_length=100)
    user = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    project = models.ForeignKey(Project, models.PROTECT)
    completed = models.BooleanField(default=False)