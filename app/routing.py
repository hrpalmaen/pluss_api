from django.urls import re_path
from .consumers import LoginConsumer


websocket_routing = [
	re_path(r"ws$", LoginConsumer),
]