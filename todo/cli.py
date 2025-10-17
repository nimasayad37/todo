from todo.project_manager import ProjectManager
from todo.task_manager import TaskManager
from todo.models import Task, Project

#-------------------MAIN MENU---------------

def main_menu() -> None:
    while True:
        print("\n===TODO APP===")
        print("1. Manage projects")
        print("2. Manage tasks")
        print("3. Exit")
        choice = input("choose an option: ").strip()

        if choice == "1":
            project_menu()
        elif choice == "2":
            task_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

#--------------PROJECT MENU-----------------

def project_menu() -> None:
    while True:
        print("\n--- Project Menu ---")
        print("1. List Projects")
        print("2. Add Project")
        print("3. Edit Project")
        print("4. Remove Project")
        print("5. Back to Main Menu")

        choice = input("choose an option: ").strip()

        if choice == "1":
            list_projects()
        elif choice == "2":
            add_project()
        elif choice == "3":
            edit_project()
        elif choice == "4":
            remove_project()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

def list_projects() -> None:
    projects = ProjectManager.list_projects()
    if not projects:
        print("No projects yet.")
    else:
        print("\nProjects:")
        for i, p in enumerate(projects, start=1):
            print(f"{i}. {p.name} __ {p.description}")

def add_project() -> None:
    name = input("Project name").strip()
    description = input("Project description").strip()

    try:
        project = Project(name=name, description=description)
        msg = ProjectManager.add_project(project)
        print(msg)
    except ValueError as e:
        print(e)

def edit_project() -> None:
    old_name = input("Enter current project name:").strip()
    new_name = input("Enter new project name. (leave blank to keep):").strip() or None
    new_description = input("Enter new project description: (leave blank to keep):").strip() or None

    try:
        msg = ProjectManager.edit_project(old_name, new_name, new_description)
        print(msg)
    except ValueError as e:
        print(e)

def remove_project() -> None:
    name = input("Enter project name to remove:").strip()
    try:
        msg = ProjectManager.remove_project(name)
        print(msg)
    except ValueError as e:
        print(e)

#-------------------TASK MENU-------------

def task_menu() -> None:
    while True:
        print("\n--- Task Menu ---")
        print("1. List Tasks in Project")
        print("2. Add Task to Project")
        print("3. Edit Task")
        print("4. Remove Task")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ").strip

        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

def list_tasks() -> None:
    project_name = input("Enter project name:").strip()
    try:
        project = ProjectManager.get_project(project_name)
        tasks = TaskManager.list_tasks(project)
        if not tasks:
            print("No tasks in this project.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t.name} __{t.status} __ deadline: {t.deadline} __ description: {t.description}")
    except ValueError as e:
        print(e)

def add_task() -> None:
    project_name = input("project name:").strip()
    try:
        project = ProjectManager.get_project(project_name)
    except ValueError as e:
        print(e)
        return
    name = input("Enter new task name:").strip()
    description = input("Enter new task description:").strip()
    deadline = input("Enter new task deadline:").strip()

    try:
        task = Task(name=name, description=description, deadline=deadline)
        TaskManager.add_task(project=project, task=task)
        print(f"Task {task.name} added to project {project.name}")
    except ValueError as e:
        print(e)

def edit_task() -> None:
    project_name = input("project name:").strip()
    task_name = input("Enter new task name:").strip()

    new_name = input("Enter new task name(leave blank to keep):").strip() or None
    new_description = input("Enter new task description:(leave blank to keep):").strip() or None
    new_deadline = input("Enter new task deadline:(leave blank to keep):").strip() or None
    new_status = input("Enter new task status(todo/doing/done, leave blank to keep):").strip() or None

    try:
        project = ProjectManager.get_project(project_name)
        TaskManager.edit_task_by_name(project=project, task_name=task_name, new_name=new_name, new_description=new_description, new_deadline=new_deadline, new_status=new_status)
        print("Task updated successfully")
    except ValueError as e:
        print(e)

def remove_task() -> None:
    project_name = input("project name:").strip()
    task_name = input("Enter new task name:").strip()

    try:
        project = ProjectManager.get_project(project_name)
        msg = TaskManager.remove_task_by_name(project=project, task_name=task_name)
        print(msg)
    except ValueError as e:
        print(e)
