from django.urls import path
from .views import (
    SkillListView,
    SkillDetailView,
    SkillCreateView,
    SkillUpdateView,
    SkillDeleteView,
    UserProfileListView,
    UserProfileDetailView,
    UserProfileCreateView,
    UserProfileUpdateView,
    UserProfileDeleteView,
)

app_name = "profiles"

urlpatterns = [
    path("skill/list/", SkillListView.as_view(), name="skill_list"),
    path("skill/detail/<int:pk>", SkillDetailView.as_view(), name="skill_detail"),
    path("skill/create/", SkillCreateView.as_view(), name="skill_create"),
    path("skill/update/<int:pk>", SkillUpdateView.as_view(), name="skill_update"),
    path("skill/delete/<int:pk>", SkillDeleteView.as_view(), name="skill_delete"),
    path("userprofile/list/", UserProfileListView.as_view(), name="userprofile_list"),
    path(
        "userprofile/detail/<int:pk>",
        UserProfileDetailView.as_view(),
        name="userprofile_detail",
    ),
    path(
        "userprofile/create/",
        UserProfileCreateView.as_view(),
        name="userprofile_create",
    ),
    path(
        "userprofile/update/<int:pk>",
        UserProfileUpdateView.as_view(),
        name="userprofile_update",
    ),
    path(
        "userprofile/delete/<int:pk>",
        UserProfileDeleteView.as_view(),
        name="userprofile_delete",
    ),
]
