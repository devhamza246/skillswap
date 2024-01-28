from os import path
from messaging.views import (
    ConversationCreateView,
    ConversationDeleteView,
    ConversationListView,
    ConversationUpdateView,
    MessageCreateView,
    MessageDeleteView,
    MessageListView,
    MessageUpdateView,
)


urlpatterns = [
    path("message/list/", MessageListView.as_view(), name="message_list"),
    path("message/detail/<int:pk>/", MessageListView.as_view(), name="message_detail"),
    path("message/create/", MessageCreateView.as_view(), name="message_create"),
    path("message/update/<int:pk>", MessageUpdateView.as_view(), name="message_update"),
    path("message/delete/<int:pk>", MessageDeleteView.as_view(), name="message_delete"),
    path("conversation/list/", MessageListView.as_view(), name="conversation_list"),
    path(
        "conversation/detail/<int:pk>/",
        ConversationListView.as_view(),
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
