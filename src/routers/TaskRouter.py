from fastapi import APIRouter,HTTPException
from uuid import UUID,uuid4
from typing import List
from models.Task import Task

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

# dummy datastore
tasks=[]

@router.post("/",response_model=Task)
def create_task(task:Task):
    task.id=uuid4()
    tasks.append(task)
    return task

@router.get("/",response_model=Task)
def get_task_by_id(task_id:UUID):
    for task in tasks:
        if task.id==task_id:
            return task
    raise HTTPException(status_code=404,detail="Task Not Found")

@router.get("/getAll",response_model=List[Task])
def get_all_tasks():
    return tasks

@router.put("/{task_id}",response_model=Task)
def update_task(task_id:UUID,task_update:Task):
    for idx,task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(update=task_update.model_dump(exclude_unset=True))
            tasks[idx]=updated_task
            return updated_task
    raise HTTPException(status_code=404,detail="Task Not Found")

@router.delete("/{task_id}",response_model=Task)
def delete_task(task_id:UUID):
    for idx,task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(idx)
    raise HTTPException(status_code=404,detail="Task Not Found")
