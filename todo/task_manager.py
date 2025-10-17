from typing import Optional, List
from datetime import datetime

from todo.models import Task, Project
from todo.project_manager import ProjectManager

from dotenv import load_dotenv

load_dotenv()

class TaskManager:

    @staticmethod
    def add_task(project: Project, task: Task) -> None:
        project.add_task(task)

    @staticmethod
    def add_task_by_project_name(project_name: str, task: Task) -> None:
        project = ProjectManager.get_project(project_name)
        TaskManager.add_task(project, task)

    @staticmethod
    def remove_task(project: Project, task: Task) -> str:
        found = TaskManager._find_task(project, task)
        if not found:
            raise ValueError(f"cannot find task {task} found in project {project.name}")
        return project.remove_task(task)

    @staticmethod
    def remove_task_by_name(project: Project, task_name: str, occurrence: int = 1) -> str:
        matches = [t for t in project.tasks if t.name == task_name]
        if not matches:
            raise ValueError(f"no instance of {task_name} in project {project.name}")
        index = occurrence - 1
        if index < 0 or index >= len(matches):
            raise IndexError(f"index {index} is out of range (found {len(matches)} matches)")
        to_remove = matches[index]
        project.remove_task(to_remove)
        return f"Task {to_remove.name} (occurrence {occurrence}) removed from project {project.name}"

    @staticmethod
    def edit_task(project: Project,
                  task: Task,
                  new_name: Optional[str] = None,
                  new_description: Optional[str] = None,
                  new_deadline: Optional[datetime] = None,
                  new_status: Optional[str] = None
    ) -> None:
        found = TaskManager._find_task(project, task)
        if not found:
            raise ValueError(f"No matching task found in {project.name}")
        if new_name is not None:
            found.update_name(new_name)
        if new_description is not None:
            found.update_task_description(new_description)
        if new_deadline is not None:
            found.update_deadline(new_deadline)
        if new_status is not None:
            found.update_status(new_status)
        if new_name is None and new_description is None and new_deadline is None and new_status is None:
            raise ValueError("no arguments provided")

    @staticmethod
    def edit_task_by_name(project: Project,
                          task_name: str,
                          occurrence: int = 1,
                          new_name: Optional[str] = None,
                          new_description: Optional[str] = None,
                          new_deadline: Optional[datetime] = None,
                          new_status: Optional[str] = None
    ) -> None:
        matches = [t for t in project.tasks if t.name == task_name]
        if not matches:
            raise ValueError(f"no task with name {task_name} found in project {project.name}")
        index = occurrence - 1
        if index < 0 or index >= len(matches):
            raise ValueError(f"index {index} is out of range (found {len(matches)} matches)")
        to_edit = matches[index]
        TaskManager.edit_task(project,
                              to_edit,
                              new_name=new_name,
                              new_description=new_description,
                              new_deadline=new_deadline,
                              new_status=new_status)

    @staticmethod
    def list_tasks(project: Project) -> List[Task]:
        return project.tasks.copy()

    @staticmethod
    def get_task(project: Project, task: Task) -> Task:
        found = TaskManager._find_task(project, task)
        if not found:
            raise ValueError(f"No matching task found in {project.name}")
        return found

    @staticmethod
    def _find_task(project: Project, task: Task) -> Optional[Task]:
        for _task in project.tasks:
            if _task == task:
                return _task
            if (
                _task.name == task.name
                and _task.description == task.description
                and _task.deadline == task.deadline
                and _task.status == task.status
            ):
                return _task
        return None
