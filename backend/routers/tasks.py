import logging
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from backend.repository import TaskRepository
from backend.schemas import STaskAdd, STaskId, STask

routerTasks = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

@routerTasks.post("/")
async def add_task(
       task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TaskRepository.add_one_task(task)
    logger.info("Задача добавлена")
    return {"ok": True, "task_id": task_id}

@routerTasks.get("/")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all_task()
    logger.info("Задачи выведены пользователю")
    return tasks

@routerTasks.get("/{task_id}")
async def get_task(task_id: int) -> STask:
    task = await TaskRepository.find_by_id_task(task_id)
    logger.info(f"Пользователю выведена задача с id: {task_id}")
    return task

@routerTasks.get("/by-category/{category_id}")
async def get_tasks_by_category(category_id: int) -> list[STask]:
    tasks = await TaskRepository.find_tasks_by_id_category(category_id)
    logger.info(f"Пользователю выведена задача/и с id категории: {category_id}")
    return tasks

@routerTasks.delete("/{task_id}")
async def delete_task(task_id: int) -> None:
    flag = await TaskRepository.delete_one_task(task_id)
    if(flag == True):
        logger.info(f"Пользователь удалил запись с id: {task_id}")
        return {"ok": True}
    else:
        logger.info("Ошибка! попытка удалить задачу с несуществующим индексом!")
        return HTTPException(status_code=204, detail="Task not found")

@routerTasks.put("/{task_id}")
async def update_task(task_id: int, task: STask) -> STask:
    updated_task = await TaskRepository.patch_one_task(task_id, task)
    if(updated_task is None):
        logger.info("Ошибка! попытка редактировать задачу с несуществующим индексом!")
        raise HTTPException(status_code=404, detail="Task not found")
    logger.info(f"Пользователь отредактировал запись с id: {task_id}")
    return updated_task