from app.repositories.base_repository import BaseRepository
from app.models.task import Task, StatusEnum
from sqlalchemy.orm import Session
from datetime import datetime

class TaskRepository(BaseRepository):

    def create_task(self, name, description, deadline, status, project_id: int):
        task = Task(name, description, deadline, status)
        task.project_id = project_id
        return self.session.add(task)

    def get_by_id(self, task_id: int):
        return self.get(Task, task_id)

    def get_all(self):
        return self.session.query(Task).all()

    def get_overdue(self, now):
        return self.session.query(Task).filter(Task.deadline < now).all()

    def delete_task(self, task_id):
        task = self.get(Task, task_id)
        if task:
            self.delete(task)
            return True
        return False

    def mark_as_done(self, db: Session, task_id: int):
        task = self.get(Task, task_id)
        if task:
            task.status = StatusEnum.done
            db.commit()
            db.refresh(task)
        return task



