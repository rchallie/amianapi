import logging

import sources.tui.ids as ids

from textual.app import ComposeResult
from textual.widgets import Tree
from textual.widgets.tree import TreeNode

from sources.server.projects import Projects

class RoutesList(Tree):

    DEFAULT_CSS = f"""
    {__qualname__} {{
        padding-left: 2;
    }}
    """

    def __init__(self) -> None:
        super().__init__("Projects", id=ids.ROUTES_LIST)

        self.projects = Projects()

        self.root.expand()
        self.show_root = False

        for project in self.projects.get_projects_list():
            logging.info(project)
            project_routes = self.root.add(project.name)
            project_project_routes = project.get_all_routes()
            for route in project_project_routes:
                project_routes.add_leaf(project_project_routes[route]["name"])

    def add_project(self, project_name: str) -> None:

        project_node = self.root.add(project_name)        

        # Need to be selected two time because project_node line is -1 and changed after select_node to the good value, don't know why
        self.select_node(project_node)
        self.select_node(project_node)

        project_node.expand()
        self.post_message(self.NodeSelected(project_node))
         



