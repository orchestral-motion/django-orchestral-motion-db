from .models import Position
from channels.binding.websockets import WebsocketBinding


class PositionBinding(WebsocketBinding):

    model = Position
    stream = "position"
    fields = ["timestamp", "x", "y", "z"]

    @classmethod
    def group_names(cls, instance):
        return ["binding.positions"]

    def has_permission(self, user, action, pk):
        return True
