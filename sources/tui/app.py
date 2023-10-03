import sources.tui.ids as ids

from textual.app import App, ComposeResult
from textual.widgets import Label, Static, Input, Button, ContentSwitcher, Tree
from textual.containers import Horizontal, Vertical, Container

from .routes_list import RoutesList
from .project.new_project import NewProject
from .project.resume import ResumeProject

from sources.server.projects import Projects

import logging

class TUI(App):

    debug=True
    CSS_PATH='liveedit.css'

    DEFAULT_CSS = f"""
    {__qualname__} #{ids.LEFT_PANE} {{
        width: 0.5fr;
        max-width: 40;
        background: $panel;
    }}

    {__qualname__} #{ids.LEFT_PANE} Label {{
        content-align: center middle;
        height: 4;
        width: 100%;
        border-bottom: heavy gray;
        margin-bottom: 1;
        text_style: bold;
    }}

    {__qualname__} #{ids.MAIN_PANE} {{
        height: 100%;
        align: center middle;
    }}
    """

    def compose(self) -> ComposeResult:

        with Horizontal():
            with Vertical(id=ids.LEFT_PANE):
                yield Label("Am I An API ?")
                yield RoutesList()
            with ContentSwitcher(id=ids.MAIN_PANE, initial=ids.NEW_PROJECT):
                yield NewProject()
                yield ResumeProject()

    def on_button_pressed(self, event: Button.Pressed) -> None:

        match event.button.id:

            case ids.NEW_PROJECT_CREATE_BUTTON:

                project_name = self.query_one(f"#{ids.NEW_PROJECT_INPUT_FIELD}").value
                new_project_return = Projects().new_project(project_name=project_name)
                
                if new_project_return[0] == None:
                    self.query_one(NewProject).display_error(error=new_project_return[1])
                else:
                    self.query_one(RoutesList).add_project(project_name)

    # Projects Navlist 
    def on_tree_node_selected(self, event: Tree.NodeSelected):

        logging.info(f"Node: {event.node.label}")
        self.query_one(ResumeProject).set_project(event.node.label)
        self.query_one(f"#{ids.MAIN_PANE}").current = ids.RESUME_PROJECT