from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User, Todo, Project
from .serializers import UserModelSerializer, TodoModelSerializer, ProjectModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


