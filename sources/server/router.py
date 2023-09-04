from .route_inventory import RouteInventory

class Router():

    def __init__(self) -> None:
        self.routes = RouteInventory()

    def add_route(self, path, body, status_code, content_type) -> None:
        '''Jump to RouteInventory add route function.'''

        self.routes.add_route(path, body, status_code, content_type)

    def get_route(self, path) -> str:
        '''Jump to RouteInventory get route function.'''

        return self.routes.get_route(path)

    def has_route(self, path) -> bool:
        '''Jump to RouteInventory has route function.'''

        return self.routes.has_route(path)

