from pydantic import BaseModel, Field, ConfigDict
from datetime import date, datetime

class SCategoryAdd(BaseModel):
    name: str

class SCategory(SCategoryAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)

class SCategoryId(BaseModel):
    ok: bool = True
    task_id:int

class STaskAdd(BaseModel):
    name: str
    description: str = Field(None, max_length=100)
    from_time: datetime
    to_time: datetime
    priority: int = Field(..., ge=1, le=5)
    status: bool
    category_id: int | None

class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)

class STaskId(BaseModel):
    ok: bool = True
    task_id:int