from rest_framework import viewsets
from .common import User
from rest_framework.permissions import IsAdminUser
from users.serializers.UserSerializer import UserSerializer
from users.serializers.RegisterSerializer import RegisterSerializer
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)

    @action(
        serializer_class=RegisterSerializer,
        detail=False,
        url_name='register',
        url_path='register',
        methods=['POST']
    )
    def register(self, request):
        return self.create(request)
