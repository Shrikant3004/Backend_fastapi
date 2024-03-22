```markdown
# FastAPI CRUD Application with Authentication

This is a simple CRUD (Create, Read, Update, Delete) application built using FastAPI, a modern web framework for building APIs with Python. It includes endpoints that require user authentication.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Shrikant3004/Backend_fastapi.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Backend_fastapi
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the FastAPI server:
   ```bash
   uvicorn application.api:app --reload
   ```
   This will start the FastAPI server on `http://localhost:8000` by default.

2. Open your web browser and go to `http://localhost:8000/docs` to access the Swagger UI for testing the API endpoints.

3. You can also use tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/) for testing the API endpoints.

## API Endpoints

- `GET /tasks/{id}`:
  - Description: Retrieve tasks for a user by ID.
  - Parameters: 
    - `id`: ID of the user for which tasks are being retrieved.
  - Authentication Required: Yes

- `POST /users`:
  - Description: Create a new user.
  - Payload:
    - `username`: Username of the new user.
    - `password`: Password of the new user.
  - Authentication Required: No

- `POST /tasks`:
  - Description: Create a new task for a user.
  - Payload:
    - `task`: Description of the task.
    - `status` (optional): Status of the task (default is "incomplete").
  - Authentication Required: Yes

- `DELETE /tasks/{id}`:
  - Description: Delete a task by ID.
  - Parameters: 
    - `id`: ID of the task to be deleted.
  - Authentication Required: Yes

- `PUT /tasks/{id}`:
  - Description: Update a task by ID.
  - Parameters:
    - `id`: ID of the task to be updated.
  - Payload:
    - `task`: Updated description of the task.
    - `status` (optional): Updated status of the task.
  - Authentication Required: Yes

For detailed documentation on how to use each endpoint, refer to the Swagger UI (`http://localhost:8000/docs`).

## Project Structure

- `api.py`: Main FastAPI application file containing API routes.
- `config.py`: Defines schema for environment variables.
- `hashing.py`: Returns Hashed password and verify hashed password. 
- `models.py`: Defines Sqlalchemy models/tables.
- `database.py`: Handles database connection and models using SQLAlchemy.
- `oauth2.py`: Create and verify access token as well as returns id of current logged in user.
- `schema.py`: Defines Pydantic request and response schema.
- `routers.users.py`: Define endpoints for creating users.
- `routers.tasks.py`: Define endpoints related to tasks.
- `routers.auth.pu` : Defines login endpoint.
- `requirements.txt`: List of Python dependencies required for the project.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
