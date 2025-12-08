from datetime import datetime
from app.db.session import SessionLocal
from app.repositories.task_repository import TaskRepository

def close_overdue_tasks():
    db = SessionLocal()
    task_repository = TaskRepository(db)
    now = datetime.now()
    overdue_tasks = task_repository.get_overdue(now)
    for task in overdue_tasks:
        task.status = "done"
        db.commit()
        db.refresh(task)
    db.close()