from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import (
    ConversationListSerializer,
    MessageSerializer,
    ConversationSerializer,
)
from django.db.models import Count
from django.contrib.auth import get_user_model

User = get_user_model()


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def send_message(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        message_data = serializer.validated_data

        # Save the message instance
        message = Message.objects.create(**message_data)

        # Check if a conversation already exists with these participants
        existing_conversation = Conversation.objects.filter(
            participants__in=[message.sender, message.receiver]
        ).distinct()

        if existing_conversation.exists():
            # Conversation already exists
            conversation = existing_conversation.first()
        else:
            # Create a new conversation instance
            conversation = Conversation.objects.create(last_message=message)

            # Add participants to the conversation
            conversation.participants.add(message.sender, message.receiver)

        # Assign the message instance to the last_message field of the conversation
        conversation.last_message = message
        conversation.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_action_class = {"list": ConversationListSerializer}
    serializer_class = ConversationSerializer

    def get_serializer_class(self):
        if self.action in self.serializer_action_class:
            return self.serializer_action_class[self.action]
        return super().get_serializer_class()

    def get_queryset(self):
        return self.queryset.filter(participants__in=[self.request.user])

    def create(self, request, *args, **kwargs):
        data = request.data
        current_user = request.user.id
        second_user = User.objects.get(id=data["receiver"]).id
        existing_conversation = Conversation.objects.filter(
            participants__id=current_user
        ).filter(participants__id=second_user)
        if existing_conversation.exists():
            conversation = existing_conversation.first()
        else:
            conversation = Conversation.objects.create()
            conversation.participants.add(request.user.id, data["receiver"])
        return Response(ConversationSerializer(conversation).data)
