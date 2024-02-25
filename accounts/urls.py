from django.urls import path
from .views import (
    SkillAndInterestListView,
    SkillAndInterestDetailView,
    SkillAndInterestCreateView,
    SkillAndInterestUpdateView,
    SkillAndInterestDeleteView,
    UserDetailView,
    UserUpdateView,
    add_interest_view,
    add_skills_view,
    login_view,
    register_user,
)
from .viewsets import SkillAndInterestViewSet, UserViewSet
from rest_framework import routers
from django.contrib.auth.views import LogoutView

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("skillandinterest", SkillAndInterestViewSet)

app_name = "accounts"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user/detail/<int:pk>", UserDetailView.as_view(), name="user_detail"),
    path("user/update/<int:pk>", UserUpdateView.as_view(), name="user_update"),
    path(
        "user/add/interest/<int:pk>",
        add_interest_view,
        name="add_userinterest",
    ),
    path(
        "user/add/skills/<int:pk>",
        add_skills_view,
        name="add_userskills",
    ),
    path(
        "skillandinterest/list/",
        SkillAndInterestListView.as_view(),
        name="skillandinterest_list",
    ),
    path(
        "skillandinterest/detail/<int:pk>",
        SkillAndInterestDetailView.as_view(),
        name="skillandinterest_detail",
    ),
    path(
        "skillandinterest/create/",
        SkillAndInterestCreateView.as_view(),
        name="skillandinterest_create",
    ),
    path(
        "skillandinterest/update/<int:pk>",
        SkillAndInterestUpdateView.as_view(),
        name="skillandinterest_update",
    ),
    path(
        "skillandinterest/delete/<int:pk>",
        SkillAndInterestDeleteView.as_view(),
        name="skillandinterest_delete",
    ),
]
