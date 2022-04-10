from django.contrib import admin
from .models import User, Todo, Project

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Todo)