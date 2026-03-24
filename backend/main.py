from fastapi import FastAPI
from contextlib import  asynccontextmanager
from database import create_tables, delete_tables
from route import routerTasks as tasks_router
from route import routerCategory as categorys_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")
app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
app.include_router(categorys_router)





# 2025-03-20T10:00:00
# 2025-03-20T11:30:00