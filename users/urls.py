from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='users_list'),
    path('create/', UserCreateAPIView.as_view(), name='create_user'),
    path('view/<int:pk>/', UserRetrieveAPIView.as_view(), name='view_user'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update_user'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='delete_user'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]