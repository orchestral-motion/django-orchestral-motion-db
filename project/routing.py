from channels.routing import route, route_class
from accelerometer.consumers import Demultiplexer


channel_routing = [
    route_class(Demultiplexer, path='^/stream/?$'),
]
