from rest_framework import serializers
from managment.models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        exclude = []
