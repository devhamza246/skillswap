from django.urls import path
from .views import *
from .viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

app_name = "accounts"

urlpatterns = [
    path("register/", RegisterView.register, name="register"),
    path("login/", LoginView.login, name="login"),
    path("signout/", SignoutView.signout, name="signout"),
    path("reset_password/", ResetPasswordView.reset_password, name="reset_password"),
    path(
        "verify_reset_password/<uidb64>/<token>/",
        VerifyPasswordResetView.verify_password_reset,
        name="verify_reset_password",
    ),
]
