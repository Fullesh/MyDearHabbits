from django.urls import path

from habbits.apps import HabbitsConfig
from habbits.views import PublicHabbitsListAPIView, UserHabbitsListAPIView, HabbitCreateAPIView, HabbitUpdateAPIView, \
    HabbitDestroyAPIView, HabbitRetrieveAPIView

app_name = HabbitsConfig.name

urlpatterns = [
    path('habbits/', PublicHabbitsListAPIView.as_view(), name='public_habbits_list'),
    path('habbits/my/', UserHabbitsListAPIView.as_view(), name='user_habbits_list'),
    path('habbits/create/', HabbitCreateAPIView.as_view(), name='create_habbit'),
    path('habbits/update/<int:pk>/', HabbitUpdateAPIView.as_view(), name='update_habbit'),
    path('habbits/delete/<int:pk>/', HabbitDestroyAPIView.as_view(), name='delete_habbit'),
    path('habbits/<int:pk>/', HabbitRetrieveAPIView.as_view(), name='detail_habbit')
]
