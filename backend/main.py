from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware

from database import get_db, engine
import models
import schemas

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Allows all origins. Change this to specific origins like ["http://localhost:5500"] if needed.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root(request: Request, db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks


@app.post("/add")
async def add_task(request: Request, task: schemas.Task, db: Session = Depends(get_db)):
    new_task = models.Task(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.put("/change")
async def change_task(
    request: Request, task: schemas.Task, db: Session = Depends(get_db)
):
    return {"message": "Changing task"}
