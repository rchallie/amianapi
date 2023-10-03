import sources.tui.ids as ids

from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Label

class ResumeProject(Vertical):

    def __init__(self) -> None:
        super().__init__(id=ids.RESUME_PROJECT)
        self.routes = None
        self.project_name = None

    def compose(self) -> ComposeResult:
            yield Label("No project selected yet.", id="project-resume-project-name")

    def set_project(self, project_name) -> None:
        self.project_name = project_name
        self.query_one(f"#project-resume-project-name").renderable = self.project_name