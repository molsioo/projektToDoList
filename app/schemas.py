from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    created_at: datetime
    class Config:
        orm_mode = True