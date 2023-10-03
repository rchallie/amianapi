import os
import uuid
import platform
import logging

import sources.environment as Environment

from .project import Project

class Projects():

    def __init__(self):

        self.projects_path = Environment.Content.get(Environment.PROJECTS_PATH)

        # Create the project directory if it doesn't exists
        if not os.path.isdir(self.projects_path):
            os.mkdir(self.projects_path, 0o755)

            # Setup rights for non MacOS
            if platform.system() != "Darwin":
                os.chown(
                    self.projects_path,
                    pwd.getpwnam("nobody").pw_uid,
                    os.stat(self.projects_path).st_gid
                )

    def get_project(self, uuid: str) -> Project:
        '''Return an object that is the route project for 'project_name'.'''
       
        return Project(uuid)

    def get_projects_list(self) -> list:
        '''Get the projects list.'''
        
        projects = []
        for filename in os.listdir(self.projects_path):
            if os.path.isfile(os.path.join(self.projects_path, filename)):
                projects.append(self.get_project(filename.split(".json")[0]))
        return projects

    def new_project(self, project_name: str) -> tuple([Project, str]):
        '''Generate new project.'''

        if project_name == None or project_name == "":
            return (None, "Project name is empty.")

        new_project = Project(uuid=str(uuid.uuid4()))
        new_project.setup(project_name=project_name)

        return new_project, ""