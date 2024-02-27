from django.urls import path
from .viewsets import MatchUsersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("match", MatchUsersViewSet)

app_name = "matching"

urlpatterns = [
    path(
        "match/match_users/",
        MatchUsersViewSet.as_view({"get": "get_matching_users"}),
        name="match_users",
    ),
]
