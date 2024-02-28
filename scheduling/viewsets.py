from rest_framework import viewsets
from django.db.models import Q
from scheduling.filters import MeetingProposalFilter
from .models import Availability, MeetingProposal
from .serializers import (
    AvailabilitySerializer,
    MeetingProposalListSerializer,
    MeetingProposalSerializer,
)


class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer


class MeetingProposalViewSet(viewsets.ModelViewSet):
    queryset = MeetingProposal.objects.all()
    serializer_action_classes = {
        "list": MeetingProposalListSerializer,
        "create": MeetingProposalSerializer,
    }
    serializer_class = MeetingProposalSerializer
    filterset_class = MeetingProposalFilter

    def get_serializer_class(self):
        action = self.request.query_params.get("action", self.action)
        try:
            return self.serializer_action_classes[action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(Q(proposee=user) | Q(proposer=user))
