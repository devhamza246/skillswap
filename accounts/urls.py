from django.urls import path
from .views import UserDetailView, UserUpdateView, login_view, register_user
from .viewsets import UserViewSet
from rest_framework import routers
from django.contrib.auth.views import LogoutView

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user/detail/<int:pk>", UserDetailView.as_view(), name="user_detail"),
    path("user/update/<int:pk>", UserUpdateView.as_view(), name="user_update"),
]
