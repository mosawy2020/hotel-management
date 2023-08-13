from users.common import User, validated
from rest_framework import serializers
from common.validators import Confirmed


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']
