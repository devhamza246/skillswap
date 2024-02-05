from django.urls import path
from .views import (
    SkillsListView,
    SkillsDetailView,
    SkillsCreateView,
    SkillsUpdateView,
    SkillsDeleteView,
    UserDetailView,
    UserUpdateView,
    login_view,
    register_user,
)
from .viewsets import SkillViewSet, UserViewSet
from rest_framework import routers
from django.contrib.auth.views import LogoutView

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("skills", SkillViewSet)

app_name = "accounts"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user/detail/<int:pk>", UserDetailView.as_view(), name="user_detail"),
    path("user/update/<int:pk>", UserUpdateView.as_view(), name="user_update"),
    path("skill/list/", SkillsListView.as_view(), name="skill_list"),
    path("skill/detail/<int:pk>", SkillsDetailView.as_view(), name="skill_detail"),
    path("skill/create/", SkillsCreateView.as_view(), name="skill_create"),
    path("skill/update/<int:pk>", SkillsUpdateView.as_view(), name="skill_update"),
    path("skill/delete/<int:pk>", SkillsDeleteView.as_view(), name="skill_delete"),
]
