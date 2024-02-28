from rest_framework import serializers
from .models import Availability, MeetingProposal


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = "__all__"


class MeetingProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingProposal
        fields = "__all__"
