import logging

import sources.tui.ids as ids

from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Label

from sources.server.project import Project

class ResumeProject(Vertical):

    def __init__(self) -> None:
        super().__init__(id=ids.RESUME_PROJECT)
        self.routes = None
        self.project = None

    def compose(self) -> ComposeResult:
        yield Label("No project selected yet.", id="project-resume-uuid")
        yield Label("No project selected yet.", id="project-resume-project-name")

    def set_project(self, project_uuid) -> None:
        logging.info("PPPPPPPPP")
        self.project = Project(project_uuid)
        self.query_one(f"#project-resume-uuid").renderable = f"{self.project.uuid}-plop"
        self.query_one(f"#project-resume-project-name").renderable = self.project.name
