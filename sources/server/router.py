
import logging

from .projects import Projects

class Router():

    def __init__(self) -> None:

        self.projects = Projects()
        self.routes = None

    def __has_selected_project(self) -> bool:
        '''Return a boolean that return True if route inventory
        is defined with a project routes, otherwise False.'''

        return self.routes != None

    def select_project(self, uuid: str) -> None:
        '''Select 'uuid' routes inventory.'''

        self.routes = self.projects.get_inventory(uuid)

    def has_route(self, path: str) -> bool:
        '''Jump to Project has route function.'''

        # Return True to allow get route to return "Please select a project first." page.
        if self.__has_selected_project() == False:
            return True

        return self.routes.has_route(path)

    def get_route(self, path: str) -> dict:
        '''Jump to Project get route function.'''

        if self.__has_selected_project() == False:
            return {
                "path": "",
                "body": f"Please select a project first: {self.inventories.get_inventories_list()}",
                "status_code": 423,
                "content_type": "text/plain"
            }

        return self.routes.get_route(path)

    def add_route(self, path, body, status_code, content_type) -> None:
        '''Jump to Project add route function.'''

        self.routes.add_route(path, body, status_code, content_type)


    def remove_route(self, path) -> None:
        '''Jump to Project remove route function.'''

        self.routes.remove_route(path)

    def update_route(self, path, body, status_code, content_type) -> None:
        '''Jump to Project update route function.'''

        self.routes.update_route(path, body, status_code, content_type)