from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)

@router.post("/")
async def add_task(
       task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("/")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks

@router.get("/{task_id}")
async def get_task(task_id: int) -> STask:
    task = await TaskRepository.find_by_id(task_id)
    return task

@router.delete("/{task_id}")
async def delete_task(task_id: int) -> None:
    flag = await TaskRepository.delete_one(task_id)
    if(flag == True):
        return {"ok": True}
    else:
        return None