from dotenv import load_dotenv
import os
from datetime import datetime
#from app.config import Literal
from typing import Literal
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.session import Base
import enum

class StatusEnum(str, enum.Enum):
    todo = "todo"
    doing = "doing"
    done = "done"

load_dotenv(dotenv_path=".env.dev")
MAX_NUMBER_OF_TASKS = int(os.getenv("MAX_NUMBER_OF_TASK", 100))

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
    description = Column(String(150), nullable=False)
    status = Column(Enum(StatusEnum, name="task_status_enum"), nullable=False, default=StatusEnum.todo)
    deadline = Column(DateTime(timezone=False), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"))
    project = relationship("Project", back_populates="tasks")
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

