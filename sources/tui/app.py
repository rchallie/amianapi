from textual.app import App, ComposeResult
from textual.widgets import Label
from textual.containers import Horizontal

from .routes_list import RoutesList

class TUI(App):

    debug=True
    CSS_PATH='liveedit.css'

    def compose(self) -> ComposeResult:

        with Horizontal():
            yield RoutesList()