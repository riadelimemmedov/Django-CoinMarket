from django.urls import path
from .consumers import CoinConsumer

websocket_urlpatterns = [
    path('',CoinConsumer.as_asgi())
]