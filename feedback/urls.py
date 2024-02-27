from django.urls import path
from .views import (
    ReviewCreateView,
    ReviewDeleteView,
    ReviewDetailView,
    ReviewListView,
    ReviewUpdateView,
)

app_name = "feedback"

urlpatterns = [
    path("review/list/", ReviewListView.as_view(), name="review_list"),
    path("review/create/<int:reviewed_user>", ReviewCreateView.as_view(), name="review_create"),
    path("review/update/<int:pk>", ReviewUpdateView.as_view(), name="review_update"),
    path("review/detail/<int:pk>", ReviewDetailView.as_view(), name="review_detail"),
    path("review/delete/<int:pk>", ReviewDeleteView.as_view(), name="review_delete"),
]
