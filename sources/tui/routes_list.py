import sources.tui.ids as ids

from rich.segment import Segment
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Label, OptionList, Markdown

from sources.server.route_inventory import RouteInventory


class RoutesList(Vertical):

    DEFAULT_CSS = f"""
    {__qualname__} {{
        width: 0.5fr;
        max-width: 40;
    }}
    """

    def __init__(self) -> None:
        super().__init__(id=ids.ROUTES_LIST)

        self.routes_inventory = RouteInventory()
    
    @staticmethod
    def __make_route(route_path) -> Label:
        return Label(route_path)

    def compose(self) -> ComposeResult:
        for route in self.routes_inventory.get_all().values():
            yield self.__make_route(route["path"]) 
