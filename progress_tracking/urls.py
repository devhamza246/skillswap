from os import path
from .views import (
    GoalListView,
    GoalDetailView,
    GoalCreateView,
    GoalUpdateView,
    GoalDeleteView,
    ProgressUpdateListView,
    ProgressUpdateDetailView,
    ProgressUpdateCreateView,
    ProgressUpdateUpdateView,
    ProgressUpdateDeleteView,
)

urlpatterns = [
    path("goal/list/", GoalListView.as_view(), name="goal_list"),
    path("goal/detail/<int:pk>", GoalDetailView.as_view(), name="goal_detail"),
    path("goal/create/", GoalCreateView.as_view(), name="goal_create"),
    path("goal/update/<int:pk>", GoalUpdateView.as_view(), name="goal_update"),
    path("goal/delete/<int:pk>", GoalDeleteView.as_view(), name="goal_delete"),
    path(
        "progressupdate/list/",
        ProgressUpdateListView.as_view(),
        name="progressupdate_list",
    ),
    path(
        "progressupdate/detail/<int:pk>",
        ProgressUpdateDetailView.as_view(),
        name="progressupdate_detail",
    ),
    path(
        "progressupdate/create/",
        ProgressUpdateCreateView.as_view(),
        name="progressupdate_create",
    ),
    path(
        "progressupdate/update/<int:pk>",
        ProgressUpdateUpdateView.as_view(),
        name="progressupdate_update",
    ),
    path(
        "progressupdate/delete/<int:pk>",
        ProgressUpdateDeleteView.as_view(),
        name="progressupdate_delete",
    ),
]
