import json
import logging
import sources.environment as Environment

class Project():

    def __init__(self, uuid: str) -> None:

        self.project_uuid = uuid
        self.inventories_path = Environment.Content.get(Environment.PROJECTS_PATH)
        self.project_path = f"{self.inventories_path}/{self.project_uuid}.json"
        self.__pre()

    def __pre(self) -> None:
        self.project_infos = self.__load()

    def __load(self) -> None:
        '''Load data from project file.'''

        try:

            # Load data from file
            with open(self.project_path, "r") as file:
                return json.load(file)

        except FileNotFoundError:

            # Generate file if not exists
            self.project_infos = {
                "name": "",
                "uuid": self.project_uuid,
                "routes": {}
            }
            self.__save()
            return {}

        except json.decoder.JSONDecodeError:

            # Malformed json
            logging.error("Error while loading json project, please cure it.")
            exit(1)

    def __save(self):
        '''Save routes list into project file.'''

        with open(self.project_path, "w") as file:
            json.dump(self.project_infos, file, indent=4)

    @property
    def name(self):
        return self.project_infos["name"]

    @property
    def uuid(self):
        return self.project_infos["uuid"]

    def setup(self, project_name: str) -> None:
        self.__pre()

        self.project_infos["name"] = project_name
        self.__save()

        return self

    def has_route(self, path) -> bool:
        '''Return a boolean as True if route is listed in the
        inventory, otherwise return False.'''
        self.__pre()

        return path in self.project_infos["routes"]

    def get_route(self, path) -> dict:
        '''Return route informations.'''
        self.__pre()

        return self.project_infos["routes"][path]

    def get_all_routes(self) -> dict:
        '''Return all routes informations.'''
        self.__pre()

        return self.project_infos["routes"]

    def add_route(self, name, path, body, status_code, content_type) -> None:
        '''Add a route to the inventory.'''
        self.__pre()

        self.project_infos["routes"][path] = {
            "name": name,
            "path": path,
            "body": body,
            "status_code": status_code,
            "content_type": content_type
        }
        self.__save()

    def remove_route(self, path) -> None:
        '''Remove a route of the inventory.'''
        self.__pre()

        del self.project_infos["routes"][path]
        self.__save()

    def update_route(self, path, body, status_code, content_type) -> None:
        '''Update an existing route of the inventory.
        Currently just a jump to add_route.'''

        self.add_route(path, body, status_code, content_type)



    