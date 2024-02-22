from django.urls import path

from matching.views import MatchListView
from .viewsets import MatchUsersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("match", MatchUsersViewSet)

app_name = "matching"

urlpatterns = [
    path("match/list/", MatchListView.as_view(), name="match_list"),
    path(
        "match/match_users/",
        MatchUsersViewSet.as_view({"get": "get_matching_users"}),
        name="match_users",
    ),
]
