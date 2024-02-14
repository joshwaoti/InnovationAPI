from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Projects

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = ['owner', 'title', 'description', 'live']