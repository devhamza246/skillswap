from django.urls import path
from .views import (
    MatchCreateView,
    MatchDeleteView,
    MatchDetailView,
    MatchListView,
    MatchUpdateView,
    TrainedModelListView,
    TrainedModelDetailView,
    TrainedModelCreateView,
    TrainedModelUpdateView,
    TrainedModelDeleteView,
)
from .viewsets import MatchViewSet, TrainedModelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("match", MatchViewSet)
router.register("trainedmodel", TrainedModelViewSet)

app_name = "matching"

urlpatterns = [
    path("match/list/", MatchListView.as_view(), name="match_list"),
    path("match/detail/<int:pk>", MatchDetailView.as_view(), name="match_detail"),
    path("match/create/", MatchCreateView.as_view(), name="match_create"),
    path("match/update/<int:pk>", MatchUpdateView.as_view(), name="match_update"),
    path("match/delete/<int:pk>", MatchDeleteView.as_view(), name="match_delete"),
    path(
        "trainedmodel/list/", TrainedModelListView.as_view(), name="trainedmodel_list"
    ),
    path(
        "trainedmodel/detail/<int:pk>",
        TrainedModelDetailView.as_view(),
        name="trainedmodel_detail",
    ),
    path(
        "trainedmodel/delete/<int:pk>",
        TrainedModelDeleteView.as_view(),
        name="trainedmodel_delete",
    ),
]
