from .route_inventory import RouteInventory

class Router():

    def __init__(self) -> None:
        self.routes = RouteInventory()

    def has_route(self, path) -> bool:
        '''Jump to RouteInventory has route function.'''

        return self.routes.has_route(path)

    def get_route(self, path) -> dict:
        '''Jump to RouteInventory get route function.'''

        return self.routes.get_route(path)

    def add_route(self, path, body, status_code, content_type) -> None:
        '''Jump to RouteInventory add route function.'''

        self.routes.add_route(path, body, status_code, content_type)


    def remove_route(self, path) -> None:
        '''Jump to RouteInventory remove route function.'''

        self.routes.remove_route(path)

    def update_route(self, path, body, status_code, content_type) -> None:
        '''Jump to RouteInventory update route function.'''

        self.routes.update_route(path, body, status_code, content_type)