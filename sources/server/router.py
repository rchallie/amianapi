
class Router():

    def __init__(self) -> None:
        self.routes = {}

    def add_route(self, path, body, status_code, content_type) -> None:
        '''Add a route to the route.'''

        self.routes[path] = {
            "path": path,
            "body": body,
            "status_code": status_code,
            "content_type": content_type
        }

    def get_route(self, path) -> str:
        '''Return route informations.'''

        return self.routes[path]

    def has_route(self, path) -> bool:
        '''Return a boolean as True if route is listed in the
        router, otherwise return False.'''
        
        return path in self.routes

