# mysite/routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
import app.routing

channel_routing = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter(app.routing.websocket_routing)
})