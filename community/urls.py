from django.urls import path
from community.views import (
    CommunityEventCreateView,
    CommunityEventDeleteView,
    CommunityEventDetailView,
    CommunityEventListView,
    CommunityEventUpdateView,
    ForumPostCreateView,
    ForumPostDeleteView,
    ForumPostDetailView,
    ForumPostListView,
    ForumPostUpdateView,
)
from .viewsets import (
    CommunityEventViewSet,
    ForumPostViewSet,
    CommentViewSet,
    EventParticipantViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("communityevent", CommunityEventViewSet)
router.register("forumpost", ForumPostViewSet)
router.register("comment", CommentViewSet)
router.register("eventparticipant", EventParticipantViewSet)

app_name = "community"

urlpatterns = [
    # ForumPost CRUD
    path("forumpost/list/", ForumPostListView.as_view(), name="forumpost_list"),
    path("forumpost/create/", ForumPostCreateView.as_view(), name="forumpost_create"),
    path(
        "forumpost/update/<int:pk>",
        ForumPostUpdateView.as_view(),
        name="forumpost_update",
    ),
    path(
        "forumpost/detail/<int:pk>",
        ForumPostDetailView.as_view(),
        name="forumpost_detail",
    ),
    path(
        "forumpost/delete/<int:pk>",
        ForumPostDeleteView.as_view(),
        name="forumpost_delete",
    ),
    # CommunityEvent CRUD
    path(
        "communityevent/list/",
        CommunityEventListView.as_view(),
        name="communityevent_list",
    ),
    path(
        "communityevent/create/",
        CommunityEventCreateView.as_view(),
        name="communityevent_create",
    ),
    path(
        "communityevent/update/<int:pk>",
        CommunityEventUpdateView.as_view(),
        name="communityevent_update",
    ),
    path(
        "communityevent/detail/<int:pk>",
        CommunityEventDetailView.as_view(),
        name="communityevent_detail",
    ),
    path(
        "communityevent/delete/<int:pk>",
        CommunityEventDeleteView.as_view(),
        name="communityevent_delete",
    ),
]
