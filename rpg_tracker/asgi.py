"""
ASGI config for rpg_tracker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rpg_tracker.settings')
django.setup()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from rpg_tracker.chat import routing as chat_rout
from rpg_tracker.core import routing as core_rout
from django.core.asgi import get_asgi_application

application = ProtocolTypeRouter({
    "http" : get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat_rout.websocket_urlpatterns + core_rout.websocket_urlpatterns
        )
    ),
})
