from django_filters import rest_framework as filters
from .models import Availability, MeetingProposal


class AvailabilityFilter(filters.FilterSet):
    class Meta:
        model = Availability
        fields = "__all__"


class MeetingProposalFilter(filters.FilterSet):
    class Meta:
        model = MeetingProposal
        fields = "__all__"
