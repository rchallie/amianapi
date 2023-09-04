import json
import logging
import sources.environment as Environment

class RouteInventory():

    def __init__(self) -> None:

        self.inventory_path = Environment.Content.get(Environment.INVENTORY_PATH)
        self.__pre()

    def __pre(self) -> None:
        self.routes = self.__load()

    def __load(self) -> None:
        '''Load data from inventory file.'''

        try:

            # Load data from file
            with open(self.inventory_path, "r") as file:
                return json.load(file)

        except FileNotFoundError:

            # Generate file if not exists
            self.routes = {}
            self.__save()
            return {}

        except json.decoder.JSONDecodeError:

            # Malformed json
            logging.error("Error while loading json inventory, please cure it.")
            exit(1)

    def __save(self):
        '''Save routes list into inventory file.'''

        with open(self.inventory_path, "w") as file:
            json.dump(self.routes, file, indent=4)

    def add_route(self, path, body, status_code, content_type) -> None:
        '''Add a route to the inventory.'''
        self.__pre()

        self.routes[path] = {
            "path": path,
            "body": body,
            "status_code": status_code,
            "content_type": content_type
        }
        self.__save()

    def get_route(self, path) -> str:
        '''Return route informations.'''
        self.__pre()

        return self.routes[path]

    def has_route(self, path) -> bool:
        '''Return a boolean as True if route is listed in the
        inventory, otherwise return False.'''
        self.__pre()

        return path in self.routes
    