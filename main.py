from fastapi import FastAPI 
from datetime import datetime 
from pydantic import BaseModel 
import uuid 
from fastapi import HTTPException
from typing import Optional 


app = FastAPI()

class TaskCreate(BaseModel):
    title : str
    description : str
    status : str
    priority : str 


tasks = {}
# changed from list to dictionary for better id lookup 

@app.post('/tasks')
def create_task(task : TaskCreate):
    task_id = str(uuid.uuid4())

    new_task = {
        "id" : task_id,
        "title" : task.title,
        "description" : task.description,
        "status" : task.status,
        "priority" : task.priority,
        "created_at" : datetime.utcnow().isoformat()
    }

    tasks[task_id] = new_task 
    return new_task

@app.get('/tasks/{task_id}')
def get_task_by_id(task_id: str):
    if task_id in tasks:
        return tasks[task_id]

    else:
        raise HTTPException(status_code = 404, detail='Task not found.')


@app.get('/tasks')
def get_tasks():
        return list(tasks.values())


@app.delete('/tasks/{task_id}')
def delete_task(task_id: str):
    if task_id in tasks:
        del tasks[task_id]
        return 

    else:
        raise HTTPException(status_code = 404, detail='Task not found') 



# create new model for task update 
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None 


@app.patch('/tasks/{task_id}')
def update_task_by_id(task_id: str, updates: TaskUpdate):

    if task_id not in tasks:
        raise HTTPException(status_code = 404, detail = 'Task not found.')

    task = tasks[task_id]

    if updates.title is not None:
        task['title'] = updates.title
    
    if updates.description is not None:
        task['description'] = updates.description

    if updates.status is not None:
        task['status'] = updates.status
    
    if updates.priority is not None:
        task['priority'] = updates.priority

    task['modified_at'] = datetime.utcnow().isoformat()


    return task