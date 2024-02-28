from rest_framework import serializers

from accounts.serializers import UserDropDownSerializer
from .models import Availability, MeetingProposal


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = "__all__"


class MeetingProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingProposal
        fields = "__all__"


class MeetingProposalListSerializer(MeetingProposalSerializer):
    proposee = UserDropDownSerializer()
    proposer = UserDropDownSerializer()
