import sources.tui.ids as ids

from textual.app import ComposeResult
from textual.widgets import Label, Static, Input, Button
from textual.containers import Horizontal, Vertical, Container

class NewProject(Vertical):

    DEFAULT_CSS = f"""
    {__qualname__} {{
        height: auto;
        width: 60;
    }}

    # Error
    {__qualname__} #{ids.NEW_PROJECT_ERROR} {{
        height: 0;
    }}

    {__qualname__} #{ids.NEW_PROJECT_ERROR_TITLE} {{
        height: auto;
    }}

    {__qualname__} #{ids.NEW_PROJECT_ERROR_TITLE} Label {{
        content-align: center middle;
        height: 3;
        padding-left: 2;
        padding-right: 2;
        color: crimson;
    }}

    {__qualname__} #{ids.NEW_PROJECT_ERROR_TITLE_LEFT_CORNER} {{
        align-vertical: bottom;
        height: 3;
        width: 1fr;
    }}

    {__qualname__} #{ids.NEW_PROJECT_ERROR_TITLE_LEFT_CORNER} Static {{
        border-top: heavy crimson;
        border-left: heavy crimson;
    }}

    {__qualname__} #{ids.NEW_PROJECT_ERROR_TITLE_RIGHT_CORNER} {{
        align-vertical: bottom;
        height: 3;
        width: 1fr;
    }}

    {__qualname__} #{ids.NEW_PROJECT_ERROR_TITLE_RIGHT_CORNER} Static {{
        border-top: heavy crimson;
        border-right: heavy crimson;
    }}

    {__qualname__} #{ids.NEW_PROJECT_ERROR_TEXT} {{
        color: crimson;
        width: 100%;
        content-align: center middle;
        border-left: heavy crimson;
        border-right: heavy crimson;
        border-bottom: heavy crimson;
        padding-bottom: 1;
    }}

    # Form
    {__qualname__} #{ids.NEW_PROJECT_TITLE} {{
        height: auto;
    }}

    {__qualname__} #{ids.NEW_PROJECT_TITLE} Label {{
        content-align: center middle;
        height: 3;
        padding-left: 2;
        padding-right: 2;
    }}

    {__qualname__} #{ids.NEW_PROJECT_TITLE_LEFT_CORNER} {{
        align-vertical: bottom;
        height: 3;
        width: 1fr;
    }}

    {__qualname__} #{ids.NEW_PROJECT_TITLE_LEFT_CORNER} Static {{
        border-top: heavy gray;
        border-left: heavy gray;
    }}

    {__qualname__} #{ids.NEW_PROJECT_TITLE_RIGHT_CORNER} {{
        align-vertical: bottom;
        height: 3;
        width: 1fr;
    }}

    {__qualname__} #{ids.NEW_PROJECT_TITLE_RIGHT_CORNER} Static {{
        border-top: heavy gray;
        border-right: heavy gray;
    }}

    {__qualname__} #{ids.NEW_PROJECT_INPUT} {{
        height: auto;
        border-left: heavy gray;
        border-right: heavy gray;
        padding-right: 3;
        padding-left: 3;
        padding-bottom: 2;
        padding-top: 1;
    }}

    {__qualname__} #{ids.NEW_PROJECT_INPUT} Label {{
        width: 0.75fr;
        height: 3;
        content-align: right middle;
    }}

    {__qualname__} #{ids.NEW_PROJECT_INPUT} #{ids.NEW_PROJECT_INPUT_FIELD} {{
        width: 2fr;
    }}

    {__qualname__} #{ids.NEW_PROJECT_CREATE} {{
        height: auto;
    }}

    {__qualname__} #{ids.NEW_PROJECT_CREATE} Button {{
        width: 2fr;
        border: tall gray;
    }}

    {__qualname__} #{ids.NEW_PROJECT_CREATE_LEFT_CORNER} {{
        height: 3;
        width: 1fr;
        padding-right: 5;
    }}

    {__qualname__} #{ids.NEW_PROJECT_CREATE_LEFT_CORNER} Static {{
        border-bottom: heavy gray;
        border-left: heavy gray;
    }}

    {__qualname__} #{ids.NEW_PROJECT_CREATE_RIGHT_CORNER} {{
        height: 3;
        width: 1fr;
        padding-left: 5;
    }}

    {__qualname__} #{ids.NEW_PROJECT_CREATE_RIGHT_CORNER} Static {{
        border-bottom: heavy gray;
        border-right: heavy gray;
    }}
    """

    def __init__(self) -> None:
        super().__init__(id=ids.NEW_PROJECT)

    def compose(self) -> ComposeResult:

        with Vertical(id=ids.NEW_PROJECT_ERROR):

            # Error Title
            with Horizontal(id=ids.NEW_PROJECT_ERROR_TITLE):
                with Container(id=ids.NEW_PROJECT_ERROR_TITLE_LEFT_CORNER):
                    yield Static()
                yield Label("Error")
                with Container(id=ids.NEW_PROJECT_ERROR_TITLE_RIGHT_CORNER):
                    yield Static()

            yield Label("", id=ids.NEW_PROJECT_ERROR_TEXT)

        # Top part
        with Horizontal(id=ids.NEW_PROJECT_TITLE):
            with Container(id=ids.NEW_PROJECT_TITLE_LEFT_CORNER):
                yield Static()
            yield Label("Create a new project")
            with Container(id=ids.NEW_PROJECT_TITLE_RIGHT_CORNER):
                yield Static()

        # Input part
        with Horizontal(id=ids.NEW_PROJECT_INPUT):
            yield Label("Project name :")
            yield Input(id=ids.NEW_PROJECT_INPUT_FIELD)

        # Submit part
        with Horizontal(id=ids.NEW_PROJECT_CREATE):
            with Container(id=ids.NEW_PROJECT_CREATE_LEFT_CORNER):
                yield Static()
            yield Button("Create", id=ids.NEW_PROJECT_CREATE_BUTTON)
            with Container(id=ids.NEW_PROJECT_CREATE_RIGHT_CORNER):
                yield Static()

    def display_error(self, error: str) -> None:
        self.query_one(f"#{ids.NEW_PROJECT_ERROR_TEXT}").renderable = error
        self.query_one(f"#{ids.NEW_PROJECT_ERROR}").styles.height = "auto"

    # def on_button_pressed(self, event: Button.Pressed) -> None:

    #     match event.button.id:

    #         case ids.NEW_PROJECT_CREATE_BUTTON:

    #             self.query_one(f"#{ids.NEW_PROJECT_ERROR}").styles.height = "auto"