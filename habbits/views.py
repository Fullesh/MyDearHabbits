from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from habbits.models import Habbit
from habbits.paginator import HabbitPaginator
from habbits.permissions import IsOwner
from habbits.serializers import HabbitSerializer


# Create your views here.

class HabbitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabbitSerializer
    permission_classes = [IsAuthenticated | IsAdminUser]

    def perform_create(self, serializer):
        new_habbit = serializer.save()
        new_habbit.owner = self.request.user
        new_habbit.save()


class HabbitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabbitSerializer
    queryset = Habbit.objects.all()
    permission_classes = [IsOwner | IsAdminUser]


class HabbitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habbit.objects.all()
    permission_classes = [IsOwner | IsAdminUser]


class UserHabbitsListAPIView(generics.ListAPIView):
    serializer_class = HabbitSerializer
    permission_classes = [IsAuthenticated | IsOwner | IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            queryset = Habbit.objects.all().filter(owner=user)
        else:
            queryset = Habbit.objects.all()
        return queryset


class PublicHabbitsListAPIView(generics.ListAPIView):
    serializer_class = HabbitSerializer
    queryset = Habbit.objects.all().filter(is_public=True)
    pagination_class = HabbitPaginator


class HabbitRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HabbitSerializer
    queryset = Habbit.objects.all()
    pagination_class = HabbitPaginator
