from rest_framework import viewsets
# from .common import User
from rest_framework.permissions import IsAdminUser
from users.serializers.UserSerializer import UserSerializer
from .serializers.hotel import hotelserializer
from managment.serializers.room import roomserializer, list
from managment.serializers.room_type import room_type_serializer
from managment.serializers.amenity import accessoryserializer
from rest_framework.decorators import action

from .models import Room, RoomType, Hotel, Amenity


class RoomViewSet(viewsets.ModelViewSet):
    MAP = {
           'list': list.RoomSerializer,
           'retrieve': roomserializer.RoomSerializer,
           'create': roomserializer.RoomSerializer,
           'update': roomserializer.RoomSerializer,
           'partial_update': roomserializer.RoomSerializer,
           }

    def get_serializer_class(self):
        return self.MAP[self.action]

    queryset = Room.objects.all()
    permission_classes = (IsAdminUser,)


class HotelViewSet(viewsets.ModelViewSet):
    serializer_class = hotelserializer.HotelSerializer
    queryset = Hotel.objects.all()
    permission_classes = (IsAdminUser,)


class RoomTypeViewSet(viewsets.ModelViewSet):
    serializer_class = room_type_serializer.RoomTypeSerializer
    queryset = RoomType.objects.all()
    permission_classes = (IsAdminUser,)


class AccessoryViewSet(viewsets.ModelViewSet):
    serializer_class = accessoryserializer.AccessorySerializer
    queryset = Amenity.objects.all()
    permission_classes = (IsAdminUser,)
