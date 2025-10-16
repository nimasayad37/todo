from typing import List, Optional

from todo.models import Project

import os
from dotenv import load_dotenv

load_dotenv()

MAX_NUMBER_OF_PROJECTS = int(os.getenv("MAX_NUMBER_OF_PROJECT"))

class ProjectManager:


    _projects: List[Project] = []
    _max_number_of_projects = MAX_NUMBER_OF_PROJECTS

    @classmethod
    def add_project(
                cls,
                project: Project
                    ) -> str:
        if len(cls._projects) >= cls._max_number_of_projects:
            raise ValueError(f"cannot add more than {cls._max_number_of_projects} projects")

        if cls._find_project_by_name(project.name):
            raise ValueError(f"project with the name '{project.name}' already exists")
        cls._projects.append(project)
        return f"Project '{project.name}' added successfully"

    @classmethod
    def remove_project(
            cls,
            name: str) -> str:
        project = cls._find_project_by_name(name)
        if not project:
            raise ValueError(f"No project with name '{name}'")
        cls._projects.remove(project)
        return f"Project {name} removed successfully"

    @classmethod
    def edit_project(cls,
                old_name: str,
                new_name: Optional[str] = None,
                new_description: Optional[str] = None
                     ) -> str:
        project = cls._find_project_by_name(old_name)
        if not project:
            raise ValueError(f"No project with name '{old_name}'")

        if new_name:
            if not Project.name_checker(new_name):
                raise ValueError(f"project with name must be shorter than {Project.MAX_NAME_LENGTH}")
            if cls._find_project_by_name(new_name):
                raise ValueError(f"project with name '{new_name}' already exists")
            project.name = new_name

        if new_description:
            if not Project.description_checker(new_description):
                raise ValueError(f"project description must be shorter than {Project.MAX_DESCRIPTION_LENGTH}")
            project.description = new_description

        return f"Project '{project.name}' edited successfully"
    @classmethod
    def list_projects(cls) -> List[Project]:
        return cls._projects.copy()

    @classmethod
    def get_project(cls,
                name: str
                    ) -> Optional[Project]:
        project = cls._find_project_by_name(name)
        if not project:
            raise ValueError(f"No project with name '{name}'")
        return project

    @classmethod
    def _find_project_by_name(cls,
                        name: str
                             ) -> Optional[Project]:
        for project in cls._projects:
            if project.name == name:
                return project
        return None
