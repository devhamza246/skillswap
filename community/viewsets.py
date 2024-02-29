from rest_framework import viewsets
from .models import CommunityEvent, ForumPost
from .serializers import CommunityEventSerializer, ForumPostSerializer


class CommunityEventViewSet(viewsets.ModelViewSet):
    queryset = CommunityEvent.objects.all()
    serializer_class = CommunityEventSerializer


class ForumPostViewSet(viewsets.ModelViewSet):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
