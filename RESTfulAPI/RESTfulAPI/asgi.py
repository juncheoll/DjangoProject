# RESTfulAPI/asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RESTfulAPI.settings')

import dataTest.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # 웹소켓 라우팅을 위한 미들웨어 스택 추가
    "websocket": AuthMiddlewareStack(
        URLRouter(
            # 웹소켓 URL 라우팅 설정을 추가
            dataTest.routing.websocket_urlpatterns
        )
    ),
})
