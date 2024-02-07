from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import MessageSerializer


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
