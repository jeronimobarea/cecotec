from rest_framework import serializers
from cecotec.apps.user.models import User


class CompleteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'picture')


class BasicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')
