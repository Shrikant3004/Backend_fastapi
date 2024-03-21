from fastapi import Depends,status,HTTPException,APIRouter
from fastapi.params import Body
from .. import schema,models,database
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
) 


@router.get("/{id}",response_model=schema.task_response)
def get_task(id:int,db : Session = Depends(database.get_db)):
    tasks = db.query(models.Task).filter(models.Task.user_id == id).all()

    user_query = db.query(models.User).filter(models.User.id == id).first()
    user = {"username":user_query.username,"created_at":user_query.created_at}


    task_list = [task.task for task in tasks]
    response_model = {"user":user, "task":task_list}
    
    return schema.task_response(**response_model)


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.task_response)
def create_task(task:schema.task,db : Session = Depends(database.get_db)):

    new_task = models.Task(**(task.dict()))
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    user_query = db.query(models.User).filter(models.User.id == new_task.user_id).first()

    user = {"username":user_query.username,"created_at":datetime.now()}

    response_model = {"user":user,"task":[new_task.task]}
    response = schema.task_response(**response_model)

    return response