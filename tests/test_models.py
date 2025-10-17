import pytest
from datetime import datetime, timedelta

from todo.models import Task, Project
from todo.project_manager import ProjectManager
from todo.task_manager import TaskManager

# ---------------- TASK TESTS ----------------

def test_create_valid_task():
    deadline = datetime.now() + timedelta(days=1)
    task = Task(name="Short name", description="Short desc", deadline=deadline)
    assert task.name == "Short name"
    assert task.status == "todo"

def test_invalid_name_raises():
    deadline = datetime.now() + timedelta(days=1)
    with pytest.raises(ValueError):
        Task(name="x" * 31, description="ok", deadline=deadline)

def test_invalid_description_raises():
    deadline = datetime.now() + timedelta(days=1)
    with pytest.raises(ValueError):
        Task(name="Valid", description="x" * 151, deadline=deadline)

def test_invalid_deadline_raises():
    with pytest.raises(ValueError):
        Task(name="Valid", description="Valid", deadline="not-a-date")

def test_update_status_works():
    deadline = datetime.now() + timedelta(days=1)
    task = Task(name="t", description="d", deadline=deadline)
    task.update_status("doing")
    assert task.status == "doing"

    with pytest.raises(ValueError):
        task.update_status("invalid_status")

# ---------------- PROJECT TESTS ----------------

def test_create_project():
    project = Project(name="My Project", description="Some desc")
    assert project.name == "My Project"
    assert project.description == "Some desc"

# ---------------- PROJECT MANAGER TESTS ----------------

def test_add_and_get_project():
    ProjectManager._projects.clear()  # reset state
    p = Project(name="TestProj", description="Desc")
    ProjectManager.add_project(p)
    assert ProjectManager.get_project("TestProj") == p

def test_duplicate_project_name_raises():
    ProjectManager._projects.clear()
    p1 = Project(name="DupProj", description="Desc")
    p2 = Project(name="DupProj", description="Desc 2")
    ProjectManager.add_project(p1)
    with pytest.raises(ValueError):
        ProjectManager.add_project(p2)

# ---------------- TASK MANAGER TESTS ----------------

def test_add_task_to_project():
    ProjectManager._projects.clear()
    project = Project(name="P", description="D")
    ProjectManager.add_project(project)

    deadline = datetime.now() + timedelta(days=1)
    task = Task(name="T", description="D", deadline=deadline)

    TaskManager.add_task(project=project, task=task)
    assert TaskManager.get_task(project, task).name == "T"
