from django.urls import path
from .views import (
    AvailabilityListView,
    AvailabilityCreateView,
    AvailabilityDetailView,
    AvailabilityUpdateView,
    AvailabilityDeleteView,
    MeetingProposalListView,
    MeetingProposalCreateView,
    MeetingProposalDetailView,
    MeetingProposalUpdateView,
    MeetingProposalDeleteView,
)

app_name = "scheduling"

urlpatterns = [
    path(
        "availability/list/",
        AvailabilityListView.as_view(),
        name="availability_list",
    ),
    path(
        "availability/create/",
        AvailabilityCreateView.as_view(),
        name="availability_create",
    ),
    path(
        "availability/detail/<int:pk>",
        AvailabilityDetailView.as_view(),
        name="availability_detail",
    ),
    path(
        "availability/update/<int:pk>",
        AvailabilityUpdateView.as_view(),
        name="availability_update",
    ),
    path(
        "availability/delete/<int:pk>",
        AvailabilityDeleteView.as_view(),
        name="availability_delete",
    ),
    path(
        "meetingproposal/list/",
        MeetingProposalListView.as_view(),
        name="meetingproposal_list",
    ),
    path(
        "meetingproposal/create/",
        MeetingProposalCreateView.as_view(),
        name="meetingproposal_create",
    ),
    path(
        "meetingproposal/detail/<int:pk>",
        MeetingProposalDetailView.as_view(),
        name="meetingproposal_detail",
    ),
    path(
        "meetingproposal/update/<int:pk>",
        MeetingProposalUpdateView.as_view(),
        name="meetingproposal_update",
    ),
    path(
        "meetingproposal/delete/<int:pk>",
        MeetingProposalDeleteView.as_view(),
        name="meetingproposal_delete",
    ),
]
