from sqlalchemy import Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.asyncio import  create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime

engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class TasksOrm(Model):
    __tablename__ =  "tasks"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    from_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    to_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    priority: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, nullable=False)
    category_id: Mapped[int | None] = mapped_column(
        ForeignKey("categories.id"), nullable=True
    )
    category: Mapped["Category | None"] = relationship(
        "CategoryOrm",
        back_populates="tasks",
    )

class CategoryOrm(Model):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    tasks: Mapped[list["TasksOrm"]] = relationship(
        "TasksOrm",
        back_populates="category"
    )
async  def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async  def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)