from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from repository import TaskRepository, CategoryRepository
from schemas import STaskAdd, STask, STaskId, SCategory, SCategoryAdd, SCategoryId

routerTasks = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)

routerCategory = APIRouter(
    prefix="/category",
    tags=["Категории"],
)

@routerTasks.post("/")
async def add_task(
       task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TaskRepository.add_one_task(task)
    return {"ok": True, "task_id": task_id}

@routerTasks.get("/")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all_task()
    return tasks

@routerTasks.get("/{task_id}")
async def get_task(task_id: int) -> STask:
    task = await TaskRepository.find_by_id_task(task_id)
    return task

@routerTasks.get("/by-category/{category_id}")
async def get_tasks_by_category(category_id: int) -> list[STask]:
    tasks = await TaskRepository.find_tasks_by_id_category(category_id)
    return tasks

@routerTasks.delete("/{task_id}")
async def delete_task(task_id: int) -> None:
    flag = await TaskRepository.delete_one_task(task_id)
    if(flag == True):
        return {"ok": True}
    else:
        return HTTPException(status_code=204, detail="Task not found")

@routerTasks.put("/{task_id}")
async def update_task(task_id: int, task: STask) -> STask:
    updated_task = await TaskRepository.patch_one_task(task_id, task)
    if(updated_task is None):
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@routerCategory.post("/")
async def add_category(
       category: Annotated[SCategoryAdd, Depends()]
) -> SCategoryId:
    category_id = await CategoryRepository.add_one_category(category)
    return {"ok": True, "task_id": category_id}

@routerCategory.get("/")
async def get_categorys() -> list[SCategory]:
    categorys = await CategoryRepository.find_all_category()
    return categorys

@routerCategory.get("/{category_id}")
async def get_category(category_id: int) -> SCategory:
    category = await CategoryRepository.find_by_id_category(category_id)
    return category

@routerCategory.delete("/{category_id}")
async def delete_category(category_id: int) -> None:
    flag = await CategoryRepository.delete_one_category(category_id)
    if(flag == True):
        return {"ok": True}
    else:
        return HTTPException(status_code=204, detail="Category not found")

@routerCategory.put("/{category_id}")
async def update_category(category_id: int, category: SCategory) -> SCategory:
    updated_category = await CategoryRepository.patch_one_category(category_id, category)
    if(updated_category is None):
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_category