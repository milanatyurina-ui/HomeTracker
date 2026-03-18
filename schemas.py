from pydantic import BaseModel, Field, ConfigDict
from datetime import date, datetime


class STaskAdd(BaseModel):
    name: str
    description: str = Field(None, max_length=100)
    from_time: datetime
    to_time: datetime
    priority: int = Field(..., ge=1, le=5)
    status: bool
class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)

class STaskId(BaseModel):
    ok: bool = True
    task_id:int