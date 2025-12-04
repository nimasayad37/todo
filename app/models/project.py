from dotenv import load_dotenv
from task import Task
from app.config import os, List

load_dotenv()
MAX_NUMBER_OF_TASKS = int(os.getenv("MAX_NUMBER_OF_TASK"))

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

