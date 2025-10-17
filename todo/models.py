from typing import Literal, List
from datetime import datetime
import os

from dotenv import load_dotenv

load_dotenv()

MAX_NUMBER_OF_TASKS = int(os.getenv("MAX_NUMBER_OF_TASK"))

class Task:
    MAX_NAME_LENGTH = 30
    MAX_DESCRIPTION_LENGTH = 150
    ALLOWED_STATUS_CHOICES = ["todo", "done", "doing"]
    @staticmethod
    def name_checker(name: str) -> bool:
        if len(name) > Task.MAX_NAME_LENGTH:
            return False
        return True
    @staticmethod
    def description_checker(description: str) -> bool:
        if len(description) > Task.MAX_DESCRIPTION_LENGTH:
            return False
        return True
    @staticmethod
    def deadline_checker(deadline) -> bool:
        if isinstance(deadline, datetime):
            return True
        return False
    @staticmethod
    def status_checker(status: str) -> bool:
        if status not in Task.ALLOWED_STATUS_CHOICES:
            return False
        return True


    def __init__(
            self,
            name: str,
            description: str,
            deadline: datetime,
            status:Literal["todo", "doing", "done"] = "todo"
            ):

        if not self.name_checker(name):
            raise ValueError(f"Task name must be at most {Task.MAX_NAME_LENGTH} characters long")
        self.name = name

        if not self.description_checker(description):
            raise ValueError(f"Task description must be at most {Task.MAX_DESCRIPTION_LENGTH} characters long")
        self.description = description

        if not self.deadline_checker(deadline):
            raise ValueError(f"Deadline must be a datetime object")
        self.deadline = deadline

        if not self.status_checker(status):
            raise ValueError(f"Status must be one of {Task.ALLOWED_STATUS_CHOICES}")
        self.status = status

    def update_status(self, status):
        if not Task.status_checker(status):
            raise ValueError(f"Status must be one of {Task.ALLOWED_STATUS_CHOICES}")
        self.status = status

    def update_name(self, name):
        if not Task.name_checker(name):
            raise ValueError(f"Task name must be at most {Task.MAX_NAME_LENGTH} characters long")
        self.name = name

    def update_task_description(self, description):
            if not Task.description_checker(description):
                raise ValueError(f"Task description must be at most {Task.MAX_DESCRIPTION_LENGTH} characters long")
            self.description = description

    def update_deadline(self, deadline):
        if not Task.deadline_checker(deadline):
            raise ValueError(f"Deadline must be a datetime object")
        self.deadline = deadline


class Project:
    MAX_NAME_LENGTH = 30
    MAX_DESCRIPTION_LENGTH = 150
    @staticmethod
    def name_checker(name: str) -> bool:
        if len(name) > Project.MAX_NAME_LENGTH:
            return False
        return True
    @staticmethod
    def description_checker(description: str) -> bool:
        if len(description) > Project.MAX_DESCRIPTION_LENGTH:
            return False
        return True

    def __init__(self, name: str, description: str):

        if not Project.name_checker(name):
            raise ValueError(f"Project name must be at most {Project.MAX_NAME_LENGTH} characters long")
        self.name = name

        if not Project.description_checker(description):
            raise ValueError(f"Project description must be at most {Project.MAX_DESCRIPTION_LENGTH} characters long")
        self.description = description

        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        if len(self.tasks) == MAX_NUMBER_OF_TASKS:
            raise ValueError(f"Cannot add task with {len(self.tasks)} tasks")
        self.tasks.append(task)

    def remove_task(self, task: Task) -> str:
        if task not in self.tasks:
            raise ValueError(f"Task {task} does not exist")
        self.tasks.remove(task)
        return f"Task {task.name} removed from {self.name}"

    def update_name(self, name):
        if not Project.name_checker(name):
            raise ValueError(f"Project name must be at most {Project.MAX_NAME_LENGTH} characters long")
        self.name = name

    def update_description(self, description):
        if not Project.description_checker(description):
            raise ValueError(f"Description must be at most {Project.MAX_DESCRIPTION_LENGTH} characters long")
        self.description = description







