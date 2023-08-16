from django.db import models


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    objects = models.Manager()

    class Meta:
        abstract = True


class NameDesModel(models.Model):
    name = models.CharField(max_length=255)
    des = models.TextField()

    class Meta:
        abstract = True
