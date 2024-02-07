"""
ASGI config for conf project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import messaging.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

# application = get_asgi_application()
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(messaging.routing.websocket_urlpatterns),
    }
)
