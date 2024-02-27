from .viewsets import MatchUsersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("match", MatchUsersViewSet)

app_name = "matching"

urlpatterns = []
