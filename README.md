📌 To-Do List API with FastAPI + PostgreSQL
This project is a simple To-Do List application built using FastAPI
 and PostgreSQL
It allows you to create, read, update, and delete (CRUD) to-do tasks. The main idea is to show how a small project can connect a web API (FastAPI) with a database (PostgreSQL) and make it accessible via Swagger UI (for testing) and pgAdmin4 (for database management).
Even if you are non-technical, this README will walk you through every single step: what the project is, how to set it up, and how to use it.
🌍 Why This Project?
Most people are used to keeping their daily tasks in a diary, notes app, or sticky notes. This project does the same thing but in a professional, software-developer way:
Instead of paper → we use a database.
Instead of pen → we use APIs.
Instead of reading tasks in a diary → we view them on Swagger UI or pgAdmin4.

🛠️ What You Need Before Running
just follow the checklist:
Install Python (version 3.10 or higher)
👉 Download from python.org
.
After installation, check it works by running:
python --version
Install PostgreSQL & pgAdmin4
👉 Download from postgresql.org/download
PostgreSQL is the actual database engine.
pgAdmin4 is a graphical tool to view and manage the database easily.
Install VS Code
👉 Download from code.visualstudio.com
.
This will make editing and running the code easier.

Install FastAPI and Uvicorn
Inside your project folder, open the terminal and run:

pip install fastapi uvicorn psycopg2-binary sqlalchemy pydantic

How the Project Works (Simple Explanation)

You create a task
Example: “Buy groceries”.

FastAPI receives your request
FastAPI is like the receptionist who notes down your request.

The task gets stored in PostgreSQL
PostgreSQL is like the cupboard where all your tasks are kept safely.

You can later retrieve, update, or delete tasks
Just like opening the cupboard, changing your notes, or throwing away old ones.

 How to Run This Project
Step 1: Clone or Download the Project

If you have Git:

git clone https://github.com/your-username/to-do-api.git
cd to-do-api

Step 2: Create the Database in PostgreSQL

Open pgAdmin4.

Login with your username/password (default user is postgres).

Create a new database:

CREATE DATABASE todo_db;

Step 3: Configure Database URL

Open to_do_api.py and edit this line:

DATABASE_URL = "postgresql://postgres:yourpassword@localhost:5432/todo_db"


Replace yourpassword → your actual PostgreSQL password.

Replace todo_db → the database you just created.

Step 4: Run the FastAPI Server

In terminal:

uvicorn to_do_api:app --reload


If successful, you’ll see:

INFO:     Uvicorn running on http://127.0.0.1:8000

Step 5: Open Swagger UI (User-Friendly Testing)

Go to your browser:
👉 http://127.0.0.1:8000/docs

Here you’ll see buttons for each action:

POST /todos/ → Add a new task

GET /todos/ → View all tasks

GET /todos/{id} → View a specific task

PUT /todos/{id} → Update a task

DELETE /todos/{id} → Delete a task

All you need to do is click “Try it out” → enter data → click Execute.

Step 6: View Data in pgAdmin4

Open pgAdmin4.

Select your database (todo_db).

Open Query Tool and run:

SELECT * FROM todos;


You will see the tasks you created via Swagger UI.

🔄 Example Workflow

Create a task:

Go to POST /todos/ in Swagger.

Enter:

{
  "title": "Finish assignment",
  "description": "Complete by Sunday"
}


Execute → You’ll see a response like:

{
  "id": 1,
  "title": "Finish assignment",
  "description": "Complete by Sunday"
}


Check in pgAdmin4:

SELECT * FROM todos;


You’ll see:

id | title             | description
---------------------------------------
1  | Finish assignment | Complete by Sunday


Update the task:

Use PUT /todos/1.

Change description → "Complete by Saturday instead".

Delete the task:

Use DELETE /todos/1.

Run the query again in pgAdmin → Task is gone.

🧑‍💻 Technical Details (for Developers)

Framework: FastAPI (Python 3.10+)

Database: PostgreSQL 14+

ORM: SQLAlchemy

Schemas: Pydantic

DROP TABLE IF EXISTS todos;
Then restart FastAPI → table will be auto-created again.
