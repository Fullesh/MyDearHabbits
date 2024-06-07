from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from users.models import User
from users.permissions import IsCreator
from users.serializers import CreateUserSerializer, UserSerializer


# Create your views here.

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsCreator | IsAdminUser]


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsCreator | IsAdminUser]
