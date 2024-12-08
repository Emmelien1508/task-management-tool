from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request

from database import get_db, engine
import models
import schemas

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

static_string = "Hello world!!!!"


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


@app.delete("/remove")
async def remove_task(request: Request):
    global static_string
    static_string = ""
    return {"message": "text removed", "text": static_string}
