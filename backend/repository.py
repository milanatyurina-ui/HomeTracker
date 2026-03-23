from sqlalchemy import select, update, delete
from sqlalchemy.orm import session

from database import new_session, TasksOrm, CategoryOrm
from schemas import STaskAdd, STask, SCategoryAdd, SCategory


class TaskRepository:
    @classmethod
    async def add_one_task(cls, data: STaskAdd) -> int:
        async  with new_session() as session:
            task_dict = data.model_dump()

            task = TasksOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def delete_one_task(cls, task_id: int) -> bool:
        async with new_session() as session:

            query = select(TasksOrm).where(TasksOrm.id == task_id)
            result = await session.execute(query)
            task = result.scalar_one_or_none()
            if(task is None):
                return False

            await session.delete(task)
            await session.commit()
            return True

    @classmethod
    async def patch_one_task(cls, task_id: int, task_data: STask) -> STask | None:
        async with new_session() as session:
            query = (
                update(TasksOrm).where(TasksOrm.id == task_id).values(
                    **task_data.model_dump(exclude_unset=True, exclude={'id'})
                ).returning(TasksOrm)
            )
            result = await session.execute(query)
            await session.commit()
            updated_orm = result.scalar_one_or_none()
            if updated_orm:
                return STask.model_validate(updated_orm)
            return None



    @classmethod
    async def find_all_task(cls) -> list[STask]:
        async  with new_session() as session:
            query = select(TasksOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_schemas

    @classmethod
    async def find_by_id_task(cls, task_id: int) -> STask | None:
        async with new_session() as session:
            query = select(TasksOrm).where(TasksOrm.id == task_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_by_id_category(cls, category_id: int) -> STask | None:
        async with new_session() as session:
            query = select(TasksOrm).where(TasksOrm.category_id == category_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()


class CategoryRepository:
    @classmethod
    async def add_one_category(cls, data: SCategoryAdd) -> int:
        async  with new_session() as session:
            category_dict = data.model_dump()

            category = CategoryOrm(**category_dict)
            session.add(category)
            await session.flush()
            await session.commit()
            return category.id

    @classmethod
    async def delete_one_category(cls, category_id: int) -> bool:
        async with new_session() as session:

            query = select(CategoryOrm).where(CategoryOrm.id == category_id)
            result = await session.execute(query)
            category = result.scalar_one_or_none()
            if(category is None):
                return False

            await session.delete(category)
            await session.commit()
            return True

    @classmethod
    async def patch_one_category(cls, category_id: int, category_data: SCategory) -> SCategory | None:
        async with new_session() as session:
            query = (
                update(CategoryOrm).where(CategoryOrm.id == category_id).values(
                    **category_data.model_dump(exclude_unset=True, exclude={'id'})
                ).returning(CategoryOrm)
            )
            result = await session.execute(query)
            await session.commit()
            updated_orm = result.scalar_one_or_none()
            if updated_orm:
                return SCategory.model_validate(updated_orm)
            return None



    @classmethod
    async def find_all_category(cls) -> list[SCategory]:
        async  with new_session() as session:
            query = select(CategoryOrm)
            result = await session.execute(query)
            category_models = result.scalars().all()
            category_schemas = [SCategory.model_validate(category_model) for category_model in category_models]
            return category_schemas

    @classmethod
    async def find_by_id_category(cls, category_id: int) -> SCategory | None:
        async with new_session() as session:
            query = select(CategoryOrm).where(CategoryOrm.id == category_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
