from rest_framework import viewsets
from .models import CommunityEvent, ForumPost, Comment, EventParticipant
from .serializers import (
    CommunityEventSerializer,
    ForumPostSerializer,
    CommentSerializer,
    EventParticipantSerializer,
)


class CommunityEventViewSet(viewsets.ModelViewSet):
    queryset = CommunityEvent.objects.all()
    serializer_class = CommunityEventSerializer


class ForumPostViewSet(viewsets.ModelViewSet):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class EventParticipantViewSet(viewsets.ModelViewSet):
    queryset = EventParticipant.objects.all()
    serializer_class = EventParticipantSerializer
