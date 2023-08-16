from rest_framework import serializers
from managment.models import RoomType


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        exclude = []
