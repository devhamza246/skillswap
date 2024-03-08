from rest_framework import serializers
from accounts.serializers import UserDropDownSerializer
from scheduling.zoom_handler import create_meeting
from .models import Availability, MeetingProposal


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = "__all__"


class MeetingProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingProposal
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.status = validated_data.get("status")
        if instance.meeting_type == MeetingProposal.Type.ONLINE:
            meeting_link = create_meeting(
                instance.proposed_time, instance.proposee.email
            )
            instance.meeting_link = meeting_link
        instance.save()
        return instance


class MeetingProposalListSerializer(MeetingProposalSerializer):
    proposee = UserDropDownSerializer()
    proposer = UserDropDownSerializer()
    meeting_type = serializers.CharField(source="get_meeting_type_display")
