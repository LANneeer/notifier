from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import (UserRegistrationAPIView, UserLoginAPIView,
                         UserLogoutAPIView, TelegramView, UserAPIView)


app_name = "users"

urlpatterns = [
    path("register/", UserRegistrationAPIView.as_view(), name="create-user"),
    path("login/", UserLoginAPIView.as_view(), name="login-user"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("logout/", UserLogoutAPIView.as_view(), name="logout-user"),
    path("", UserAPIView.as_view(), name="user-info"),
    path("telegram/", TelegramView.as_view()),
]