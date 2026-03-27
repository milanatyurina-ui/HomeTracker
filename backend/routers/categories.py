import logging
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from backend.repository import CategoryRepository
from backend.schemas import SCategoryAdd, SCategoryId, SCategory

routerCategory = APIRouter(
    prefix="/category",
    tags=["Категории"],
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

@routerCategory.post("/")
async def add_category(
       category: Annotated[SCategoryAdd, Depends()]
) -> SCategoryId:
    category_id = await CategoryRepository.add_one_category(category)
    logger.info("Категория добавлена")
    return {"ok": True, "task_id": category_id}

@routerCategory.get("/")
async def get_categorys() -> list[SCategory]:
    categorys = await CategoryRepository.find_all_category()
    logger.info("Категории выведены пользователю")
    return categorys

@routerCategory.get("/{category_id}")
async def get_category(category_id: int) -> SCategory:
    category = await CategoryRepository.find_by_id_category(category_id)
    logger.info(f"Пользователю выведена категория с id: {category_id}")
    return category

@routerCategory.delete("/{category_id}")
async def delete_category(category_id: int) -> None:
    flag = await CategoryRepository.delete_one_category(category_id)
    if(flag == True):
        logger.info(f"Пользователь удалил запись с id: {category_id}")
        return {"ok": True}
    else:
        logger.info("Ошибка! попытка удалить задачу с несуществующим индексом!")
        return HTTPException(status_code=204, detail="Category not found")

@routerCategory.put("/{category_id}")
async def update_category(category_id: int, category: SCategory) -> SCategory:
    updated_category = await CategoryRepository.patch_one_category(category_id, category)
    if(updated_category is None):
        logger.info("Ошибка! попытка редактировать категорию с несуществующим индексом!")
        raise HTTPException(status_code=404, detail="Task not found")
    logger.info(f"Пользователь отредактировал запись с id: {category_id}")
    return updated_category