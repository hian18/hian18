from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import CustomUser


class CustomUserSeralizer(ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'username','password','id']
