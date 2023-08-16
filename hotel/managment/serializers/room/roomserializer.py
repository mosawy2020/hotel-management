from rest_framework import serializers

import managment.serializers.amenity.accessoryserializer
from managment.models import Room
from managment.serializers.hotel.hotelserializer import HotelSerializer
from managment.serializers.room_type.room_type_serializer import RoomTypeSerializer
from managment.serializers.amenity.accessoryserializer import AccessorySerializer
from managment.models import Amenity, Hotel, RoomType


class RoomSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())
    room_type = serializers.PrimaryKeyRelatedField(queryset=RoomType.objects.all())
    amenities  = serializers.PrimaryKeyRelatedField(many=True,queryset=Amenity.objects.all())


    class Meta:
        model = Room
        exclude = []
