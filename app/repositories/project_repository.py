from app.repositories.base_repository import BaseRepository
from app.models.project import Project
from sqlalchemy.orm import Session, joinedload


class ProjectRepository(BaseRepository):

    def get_all(self):
        return self.session.query(Project).all()

    def get_by_id(self, project_id: int):
        return self.get(Project, project_id)

    def delete_project(self, project_id: int):
        project = self.get(Project, project_id)
        if project:
            self.delete(project)
            return True
        return False

    def get_with_task(self, project_id: int):
        return self.session.query(Project).options(joinedload(Project.tasks)).filter(Project.id == project_id).first()
