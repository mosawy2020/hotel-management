from django.db import models
from common.abstractions import BaseModel, NameDesModel


# Create your models here.

class Hotel(BaseModel, NameDesModel):
    pass


class RoomType(BaseModel, NameDesModel):
    pass


class Amenity(BaseModel, NameDesModel):
    pass


class Room(BaseModel, NameDesModel):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='rooms')
    amenities = models.ManyToManyField(Amenity, through='RoomAmenity', related_name='rooms')


class RoomAmenity(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_amenities')
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE, related_name='room_amenities')
