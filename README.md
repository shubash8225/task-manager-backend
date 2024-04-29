# Task Manager WebApp (Django Backend)

This repository contains the Django backend for the Task Manager WebApp. This backend provides RESTful APIs for managing tasks.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/task-manager-backend.git
   ```

2. **Install dependencies:**

   ```bash
   cd task-manager-backend
   pip install -r requirements.txt
   ```

3. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```
5. **Create a user:**
   I have added a command which can be used to create a user without superuser permissions which can be used to log into the Task Manager.

   ```bash
   python manage.py create_user <username> <password>
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://localhost:8000`.

## API Endpoints

- **GET /api/tasks/**: Get a list of all tasks.
- **POST /api/tasks/**: Create a new task.
- **GET /api/tasks/{id}/**: Get details of a specific task.
- **PUT /api/tasks/{id}/**: Update a specific task.
- **PATCH /api/tasks/{id}/**: Partially update a specific task.
- **DELETE /api/tasks/{id}/**: Delete a specific task.

## Authentication

The API uses Token-based authentication. To authenticate requests, include an `Authorization` header with the value `Token <your-token>`.

## Environment Variables

- `SECRET_KEY`: Django secret key.
- `DEBUG`: Debug mode (True or False).
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts.
