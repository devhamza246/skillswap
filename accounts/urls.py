from django.urls import path
from .views import *
from .viewsets import *
from rest_framework import routers
from django.contrib.auth.views import LogoutView

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

# urlpatterns = [
#     path("register/", RegisterView.register, name="register"),
#     path("login/", LoginView.login, name="login"),
#     path("signout/", SignoutView.signout, name="signout"),
#     path("reset_password/", ResetPasswordView.reset_password, name="reset_password"),
#     path(
#         "verify_reset_password/<uidb64>/<token>/",
#         VerifyPasswordResetView.verify_password_reset,
#         name="verify_reset_password",
#     ),
# ]

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
