from django.urls import path
from messaging.views import (
    ConversationCreateView,
    ConversationDeleteView,
    ConversationDetailView,
    ConversationListView,
    ConversationUpdateView,
    MessageCreateView,
    MessageDeleteView,
    MessageDetailView,
    MessageListView,
    MessageUpdateView,
)
from .viewsets import MessageViewSet

app_name = "messaging"

urlpatterns = [
    path("message/list/", MessageListView.as_view(), name="message_list"),
    path("message/detail/<int:pk>", MessageDetailView.as_view(), name="message_detail"),
    path(
        "message/create/<int:receiver>",
        MessageCreateView.as_view(),
        name="message_create",
    ),
    path("message/update/<int:pk>", MessageUpdateView.as_view(), name="message_update"),
    path("message/delete/<int:pk>", MessageDeleteView.as_view(), name="message_delete"),
    path(
        "message/send/",
        MessageViewSet.as_view({"post": "send_message"}),
        name="send_message",
    ),
    path(
        "conversation/list/", ConversationListView.as_view(), name="conversation_list"
    ),
    path(
        "conversation/detail/<int:pk>",
        ConversationDetailView.as_view(),
        name="conversation_detail",
    ),
    path(
        "conversation/create/",
        ConversationCreateView.as_view(),
        name="conversation_create",
    ),
    path(
        "conversation/update/<int:pk>",
        ConversationUpdateView.as_view(),
        name="conversation_update",
    ),
    path(
        "conversation/delete/<int:pk>",
        ConversationDeleteView.as_view(),
        name="conversation_delete",
    ),
]
