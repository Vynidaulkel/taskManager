from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import crud, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/tasks", response_model=list[schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@router.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@router.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, done: bool, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, done)

@router.delete("/tasks/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id)
