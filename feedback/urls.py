from django.urls import path
from .views import (
    ReviewCreateView,
    ReviewDetailView,
    ReviewListView,
    ReviewUpdateView,
)
from rest_framework.routers import DefaultRouter
from .viewsets import ReviewViewSet

router = DefaultRouter()
router.register("review", ReviewViewSet)

app_name = "feedback"

urlpatterns = [
    path("review/list/", ReviewListView.as_view(), name="review_list"),
    path(
        "review/create/<int:reviewed_user>",
        ReviewCreateView.as_view(),
        name="review_create",
    ),
    path("review/update/<int:pk>", ReviewUpdateView.as_view(), name="review_update"),
    path("review/detail/<int:pk>", ReviewDetailView.as_view(), name="review_detail"),
]
