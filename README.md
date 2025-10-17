# Todo App (Python CLI)

A simple command-line Todo List application built in Python using **OOP** principles.  
This project allows you to manage projects and tasks in memory with a clear CLI interface.  

---

## Features

- Create, edit, and remove **Projects**  
- Each project can have multiple **Tasks**  
- Task properties: name, description, status (`todo`, `doing`, `done`), and deadline  
- Change task status and edit task details  
- Enforce limits: maximum number of tasks per project and maximum number of projects  
- Input validation for names, descriptions, and deadlines  
- Simple CLI interface to interact with projects and tasks  

---

## Project Structure


todo_app/

│

├── todo/ # Application modules

│ ├── init.py

│ ├── models.py # Task & Project classes

│ ├── project_manager.py

│ └── task_manager.py

│

├── tests/ # Pytest unit tests

│ └── test_models.py

│

├── cli.py # Command-line interface

├── main.py # Entry point for running the CLI

├── pyproject.toml # Poetry configuration

├── poetry.lock

└── .env # Environment variables (e.g., MAX_NUMBER_OF_PROJECTS)


---

## Getting Started

### Prerequisites

- Python 3.13+  
- [Poetry](https://python-poetry.org/) for dependency management  
how to install?
poetry install

---

### Installation

1. Clone the repository:

```bash
git clone https://github.com/nimasayad37/todo.git
cd todo_app

---

