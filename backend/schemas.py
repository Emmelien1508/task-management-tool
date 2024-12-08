from pydantic import BaseModel
from datetime import datetime


class Task(BaseModel):
    id: int | None = None
    title: str | None = None
    description: str | None = None
    status: str = "To do"
    due_date: datetime | None = None

    class Config:
        from_attributes = True
