import os
import platform
import logging

import sources.environment as Environment

from .routes_inventory import RoutesInventory

class Router():

    def __init__(self) -> None:

        self.inventories_path = Environment.Content.get(Environment.INVENTORIES_PATH)

        if not os.path.isdir(self.inventories_path):
            os.mkdir(self.inventories_path, 0o755)

            if platform.system() != "Darwin":
                os.chown(
                    self.inventories_path,
                    pwd.getpwnam("nobody").pw_uid,
                    os.stat(self.inventories_path).st_gid
                )

        self.routes = None

        # self.select_project("test")

    def __has_selected_project(self) -> bool:
        return self.routes != None

    def select_project(self, project_name) -> None:
        self.routes = RoutesInventory(project_name)

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