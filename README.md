# task-management-api

### Overview

This project is a task management application consisting of:

- a RESTful backend API built with FastAPI

- a lightweight frontend interface built with HTML, CSS, and vanilla JavaScript

- **As I am extremely keen to make it accesible by everyone, I also learned to deploy the frontend and backend online.**  

---
### Demo 
- Frontend (Firebase Hosting on my personal website):<br>
https://yopxue.com/project-api-frontend/index.html

- Backend API (Render): <br>
https://task-management-api-dutb.onrender.com

- API Documentation: <br>
https://task-management-api-dutb.onrender.com/docs<br>

**Note:** On Render's free tier, the backend takes a few seconds to wake up on first request.

--- 
### API Endpoint Documentation
- Get all tasks
```
GET /tasks
```
Returns a list of all tasks. 

- Create a new task 
```
POST /tasks
```
```
#json 

{
  "title": "Task title",
  "description": "Task description",
  "status": "todo | in_progress | done",
  "priority": "low | medium | high"
}
```

- Get a task by ID 
```
GET /tasks/{task_id}
```

- Update a task (partial update allowed)
```
PATCH /tasks/{task_id}
``` 

- Delete a task 
```
DELETE /tasks/{task_id}
```

---
### Design decisions 
- In-memory storage was used instead of a database, mainly for the simplicity of the assignment. 
- Task_id will be generated randomly followed by the format of UUIDs for uniqueness. 
- **ENUMS** was used to validate useful input for task priority and status. 
- Firstly, I made the main.py and the frontend files on github, then decided to deploy the frontend on my personal website [yopxue.com/projects](https://yopxue.com/projects.html) and the backend onto [Render](https://task-management-api-dutb.onrender.com).

---
### Limitation and Future Work 
- The data is currently not persistant as they are all stored in-memory. (Could be fixed if more time is given)
- No authentication method implemented due to my lack of experience dealing with API/backend setup. 
- Could improve interface design so that it matches my website style a bit more when shwocasing this mini project. 
- Could add filtering and sorting on tasks. 