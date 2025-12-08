from app.db.session import SessionLocal
from app.repositories.project_repository import ProjectRepository
from app.models.project import Project

session = SessionLocal()
proj_repo = ProjectRepository(session)

# create a real SQLAlchemy model instance
proj = Project(name="Test Project", description="Hello there")

proj_repo.add(proj)

print("Created project:", proj.id, proj.name, proj.description)

session.close()
