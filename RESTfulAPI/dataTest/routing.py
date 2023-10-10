# dataTest/routing.py

from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/order_recode/$', consumers.OrderConsumer.as_asgi()),
]
