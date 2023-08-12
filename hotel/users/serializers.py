from .common import User
from rest_framework import serializers
from .validators import Confirmed

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',

        ]

