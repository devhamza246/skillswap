from rest_framework import serializers
from .models import CommunityEvent, ForumPost


class CommunityEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityEvent
        fields = "__all__"


class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = "__all__"
