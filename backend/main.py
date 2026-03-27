from fastapi import FastAPI
from contextlib import  asynccontextmanager
from backend.database import create_tables, delete_tables
from backend.routers.tasks import routerTasks
from backend.routers.categories import routerCategory



@asynccontextmanager
async def lifespan(app:FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")
app = FastAPI(lifespan=lifespan)
app.include_router(routerTasks)
app.include_router(routerCategory)





# 2025-03-20T10:00:00
# 2025-03-20T11:30:00