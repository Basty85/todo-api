# Todo API with FastAPI, SQLite, and Docker

## Description

This project is a simple Todo API built with FastAPI and SQLite. It provides CRUD functionality for managing todo items, with a minimal HTML frontend using Jinja2 templates. The backend persists data in an SQLite database, and the entire app can be run locally or in Docker.

---

## Features

- Create, read, and delete todos
- Data persistence with SQLite
- Simple frontend rendered with Jinja2 templates
- Asynchronous database access using `databases` and SQLAlchemy Core
- CORS enabled for development
- Docker support for easy deployment

---

## Project Structure

```bash
.
├── app
│   ├── main.py          # FastAPI app and routes
│   ├── models.py        # SQLAlchemy table definitions
│   ├── schemas.py       # Pydantic models for data validation
│   ├── db.py            # Database connection setup
│   └── templates
│       └── index.html   # Frontend HTML template
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Getting Started Local

### Prerequisites

- Python 3.10+
- Docker (optional)
- SQLite (optional, for inspecting the DB file)

### 1. Installation and running

1. Clone the repo

```bash
git clone https://github.com/Basty85/todo-api.git
cd todo-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the app locally

```bash
uvicorn app.main:app --reload
```

Open browser and visit:

```bash
http://localhost:8000
```

## Getting Started Docker

### 1. Build the Docker image

```bash
docker build -t todo-api .
```

### 2. Run the container (mapping port 8000 and persisting data)

```bash
docker run -p 8000:8000 -v $(pwd)/data:/app todo-api
```

### 3. Access the app at:

```bash
http://localhost:8000
```

## Database Details

- **Database file**: `app/todos.db`
- **Backend**: SQLite
- **ORM**: SQLAlchemy Core (with the `databases` async library)
- **Table name**: `todos`
- **Created automatically** on startup if it doesn't exist

### Table Schema

| Column | Type    | Description                        |
|--------|---------|------------------------------------|
| id     | Integer | Primary key, autoincremented       |
| title  | String  | Title of the todo (cannot be null) |
| done   | Boolean | Whether the task is completed      |

### SQL Equivalent

```sql
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done BOOLEAN DEFAULT FALSE
);
```

## Interacting with the Database Manually (optional)

You can inspect the database with the sqlite3 CLI tool:

```bash
sqlite3 app/todos.db
```

Then, in the SQLite shell:
```bash
.tables         -- Shows all tables
.schema todos   -- Show schema of the todos table
SELECT * FROM todos;  -- Show all todos
```

To exit:
```bash
.quit
```
