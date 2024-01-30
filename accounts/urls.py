from django.urls import path
from .views import *
from .viewsets import *
from rest_framework import routers
from django.contrib.auth.views import LogoutView

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/detail/<int:pk>", ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/update/<int:pk>", ProfileUpdateView.as_view(), name="profile_update"),
]
