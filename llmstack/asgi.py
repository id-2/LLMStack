import os
import sys

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from os.path import dirname, abspath, join

from apps.consumers import AppConsumer


BASE_DIR = dirname(dirname(abspath(__file__)))
sys.path.append(join(BASE_DIR, 'llmstack'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'llmstack.settings')

django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/apps/<str:app_id>', AppConsumer.as_asgi()),
        ]),
    ),
})
