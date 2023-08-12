from rest_framework import viewsets
from .common import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
