from fastapi import FastAPI 

app = FastAPI()



tasks = []

@app.post('/')
def create_task(id, title, description, status, priority, created_at):
    tasks.append({
        "id" : str(id),
        "title" : title,
        "description" : description,
        "status" : status,
        "priority" : priority,
        "created_at" : created_at 
    })
    