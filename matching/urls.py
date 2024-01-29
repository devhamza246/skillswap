from django.urls import path
from matching.views import (
    MatchCreateView,
    MatchDeleteView,
    MatchDetailView,
    MatchListView,
    MatchUpdateView,
)

app_name = "matching"

urlpatterns = [
    path("match/list/", MatchListView.as_view(), name="match_list"),
    path("match/detail/<int:pk>", MatchDetailView.as_view(), name="match_detail"),
    path("match/create/", MatchCreateView.as_view(), name="match_create"),
    path("match/update/<int:pk>", MatchUpdateView.as_view(), name="match_update"),
    path("match/delete/<int:pk>", MatchDeleteView.as_view(), name="match_delete"),
]
