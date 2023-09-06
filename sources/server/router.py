
import logging

from .inventories import Inventories

class Router():

    def __init__(self) -> None:

        self.inventories = Inventories()
        self.routes = None

        self.select_project("plop")

    def __has_selected_project(self) -> bool:
        '''Return a boolean that return True if route inventory
        is defined with a project routes, otherwise False.'''

        return self.routes != None

    def select_project(self, project_name) -> None:
        '''Select 'project_name' routes inventory.'''

        self.routes = self.inventories.get_inventory(project_name)

    def has_route(self, path) -> bool:
        '''Jump to RoutesInventory has route function.'''

        # Return True to allow get route to return "Please select a project first." page.
        if self.__has_selected_project() == False:
            return True

        return self.routes.has_route(path)

    def get_route(self, path) -> dict:
        '''Jump to RoutesInventory get route function.'''

        if self.__has_selected_project() == False:
            return {
                "path": "",
                "body": "Please select a project first.",
                "status_code": 423,
                "content_type": "text/plain"
            }

        return self.routes.get_route(path)

    def add_route(self, path, body, status_code, content_type) -> None:
        '''Jump to RoutesInventory add route function.'''

        self.routes.add_route(path, body, status_code, content_type)


    def remove_route(self, path) -> None:
        '''Jump to RoutesInventory remove route function.'''

        self.routes.remove_route(path)

    def update_route(self, path, body, status_code, content_type) -> None:
        '''Jump to RoutesInventory update route function.'''

        self.routes.update_route(path, body, status_code, content_type)