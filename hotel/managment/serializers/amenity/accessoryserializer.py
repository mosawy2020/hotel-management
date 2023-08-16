from rest_framework import serializers
from managment.models import Amenity


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        exclude = []
