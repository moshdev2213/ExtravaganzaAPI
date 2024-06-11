from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List,Optional
from uuid import UUID,uuid4

app = FastAPI(
    title="Extravaganza",
    description="dveloped as a newbie to the pythons FastAPI",
)

# the pydantic validatorModel
class Task(BaseModel):
    id:Optional[UUID]=None
    title:str
    description:Optional[str]=None
    completed:bool=False

# a dummy datastore
tasks = []

@app.get("/")
def getStatus():
    return {"message":"server online"}

@app.post("/tasks/",response_model=Task)
def createTask(task:Task):
    task.id = uuid4()
    tasks.append(task)
    return task

@app.get("/tasks/",response_model=List[Task])
def getAllTasks():
    return tasks

@app.get("/tasks/{task_id}",response_model=Task)
def getTaskById(task_id:UUID):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404,detail="Task Not Found")

@app.put("/tasks/{task_id}",response_model=Task)
def updateTask(task_id:UUID,task_update:Task):
    for idx,task in enumerate(tasks):
        if task.id==task_id:
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            tasks[idx] = updated_task
            return updated_task
    raise HTTPException(status_code=404,detail="Task NOt Found")

@app.delete("/tasks/{task_id}",response_model=Task)
def delete_task(task_id:UUID):
    for idx,task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(idx)
    raise HTTPException(status_code=404,detail="Task Not Found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8095)