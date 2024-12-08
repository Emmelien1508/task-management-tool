from database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP, text


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, nullable=False, default="To do")
    due_date = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), default=datetime.now()
    )
