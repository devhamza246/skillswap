from rest_framework import viewsets
from .models import CommunityEvent, ForumPost, Comment, EventParticipant
from .serializers import (
    CommunityEventSerializer,
    ForumPostSerializer,
    CommentSerializer,
    EventParticipantSerializer,
    ForumPostListSerializer,
    CommunityEventListSerializer,
)


class CommunityEventViewSet(viewsets.ModelViewSet):
    queryset = CommunityEvent.objects.all()
    serializer_action_class = {"list": CommunityEventListSerializer}
    serializer_class = CommunityEventSerializer

    def get_serializer_class(self):
        if self.action in self.serializer_action_class:
            return self.serializer_action_class[self.action]
        return super().get_serializer_class()


class ForumPostViewSet(viewsets.ModelViewSet):
    queryset = ForumPost.objects.all()
    serializer_action_class = {"list": ForumPostListSerializer}
    serializer_class = ForumPostSerializer

    def get_serializer_class(self):
        if self.action in self.serializer_action_class:
            return self.serializer_action_class[self.action]
        return super().get_serializer_class()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class EventParticipantViewSet(viewsets.ModelViewSet):
    queryset = EventParticipant.objects.all()
    serializer_class = EventParticipantSerializer
