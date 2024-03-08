from rest_framework import serializers
from .models import CommunityEvent, ForumPost, Comment, EventParticipant


class CommunityEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityEvent
        fields = "__all__"


class CommunityEventListSerializer(CommunityEventSerializer):
    organizer = serializers.CharField(source="organizer.get_full_name")


class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = "__all__"


class ForumPostListSerializer(ForumPostSerializer):
    author = serializers.CharField(source="author.get_full_name")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class EventParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventParticipant
        fields = "__all__"
