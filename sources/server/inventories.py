import os
import platform

import sources.environment as Environment

from .routes_inventory import RoutesInventory

class Inventories():

    def __init__(self):

        self.inventories_path = Environment.Content.get(Environment.INVENTORIES_PATH)

        # Create inventories directory if it doesn't exists
        if not os.path.isdir(self.inventories_path):
            os.mkdir(self.inventories_path, 0o755)

            # Setup rights for non MacOS
            if platform.system() != "Darwin":
                os.chown(
                    self.inventories_path,
                    pwd.getpwnam("nobody").pw_uid,
                    os.stat(self.inventories_path).st_gid
                )

    def get_inventory(self, project_name) -> RoutesInventory:
        '''Return an object that is the route inventory for 'project_name'.'''
       
        return RoutesInventory(project_name)