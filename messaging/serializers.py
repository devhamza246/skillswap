from rest_framework import serializers

from accounts.serializers import UserDropDownSerializer
from .models import Message, Conversation
from django.contrib.auth import get_user_model

User = get_user_model()


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = "__all__"


class ConversationListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ["id", "user", "updated"]

    def get_user(self, obj):
        # Assuming 'request' object is available in serializer context
        request = self.context.get("request")
        current_user = request.user if request else None

        # Retrieve all participants in the conversation
        participants = obj.participants.all()

        # Filter out the current user
        other_participants = (
            participants.exclude(id=current_user.id) if current_user else participants
        )

        # Get the name and photo of the other participants
        other_participants_data = []
        for participant in other_participants:
            participant_data = {
                "name": participant.get_full_name(),
                "photo": participant.photo.url if participant.photo else None,
            }
            other_participants_data.append(participant_data)

        return other_participants_data
