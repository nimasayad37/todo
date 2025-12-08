from app.repositories.task_repository import TaskRepository
from app.db.session import SessionLocal
from datetime import datetime
from .close_overdue import close_overdue_tasks

def autoclose_overdue():
    print("Running scheduled overdue-closing job...")
    n = close_overdue_tasks()


