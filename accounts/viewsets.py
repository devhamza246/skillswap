from .models import SkillAndInterest, User
from rest_framework import viewsets
from .serializers import SkillAndInterestSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SkillAndInterestViewSet(viewsets.ModelViewSet):
    queryset = SkillAndInterest.objects.all()
    serializer_class = SkillAndInterestSerializer
