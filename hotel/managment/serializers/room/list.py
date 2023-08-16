from rest_framework import serializers
from managment.models import Room
from managment.serializers.hotel.hotelserializer import HotelSerializer
from managment.serializers.room_type.room_type_serializer import RoomTypeSerializer
from managment.serializers.amenity.accessoryserializer import AccessorySerializer


class RoomSerializer(serializers.ModelSerializer):
    # hotel = HotelSerializer()
    # room_type = RoomTypeSerializer()
    # amenities = AccessorySerializer(many=True)

    class Meta:
        model = Room
        exclude = ['hotel', 'room_type', 'amenities']
