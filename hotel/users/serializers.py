from .common import User, validated
from rest_framework import serializers
from common.validators import Confirmed


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[Confirmed('confirm_password')])
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

    def create(self, validated_data):
        return User.objects.create(**validated(validated_data, except_these=['confirm_password']))
