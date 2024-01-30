from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from messaging.consumers import ChatConsumer

application = ProtocolTypeRouter(
    {
        "websocket": URLRouter(
            [
                path("ws/chat/<int:conversation_id>/", ChatConsumer.as_asgi()),
            ]
        ),
    }
)
