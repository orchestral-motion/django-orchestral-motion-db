from channels.generic.websockets import WebsocketDemultiplexer
from .bindings import PositionBinding


class Demultiplexer(WebsocketDemultiplexer):

    consumers = {
        "position": PositionBinding.consumer,
    }

    def connection_groups(self):
        return ["binding.positions"]
