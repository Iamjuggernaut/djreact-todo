from rest_framework.serializers import ModelSerializer
from .models import User, Project, Todo


class UserModelSerializer(ModelSerializer): 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class TodoModelSerializer(ModelSerializer):
    user = UserModelSerializer()

    class Meta:
        model = Todo
        fields = '__all__'


class ProjectModelSerializer(ModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'
