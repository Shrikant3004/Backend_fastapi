from fastapi import Depends,status,HTTPException,APIRouter,Response
from .. import schema,models,database,oauth2
from sqlalchemy.orm import Session
from datetime import datetime
router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
) 


@router.get("/{id}",response_model=schema.task_response)        #id = user_id
def get_task(id:int,db : Session = Depends(database.get_db),get_current_user = Depends(oauth2.get_current_user)):
    tasks = db.query(models.Task).filter(models.Task.user_id == id).all()

    task_of_user = db.query(models.Task).filter(models.Task.user_id == id).first()

    if task_of_user is None:
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="No task found for this user")


    if task_of_user.user_id != int(get_current_user.id):
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="invalid request for this credential")

    user_query = db.query(models.User).filter(models.User.id == id).first()
    user = {"id":user_query.id,"username":user_query.username,"created_at":user_query.created_at}


    task_list = [task.task for task in tasks]
    task_id_list = [task.id for task in tasks]
    response_model = {"user":user, "task":task_list, "task_id":task_id_list}
    
    return schema.task_response(**response_model)


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.task_response)
def create_task(task:schema.task,db : Session = Depends(database.get_db), get_current_user = Depends(oauth2.get_current_user)):

    new_task = models.Task(user_id=get_current_user.id,**(task.dict()))
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    user_query = db.query(models.User).filter(models.User.id == new_task.user_id).first()

    user = {"id":user_query.id,"username":user_query.username,"created_at":datetime.now()}

    response_model = {"user":user,"task":[new_task.task], "task_id":[new_task.id]}
    response = schema.task_response(**response_model)

    return response


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)      #id = task_id
def delete_task(id:int,db : Session = Depends(database.get_db),get_current_user = Depends(oauth2.get_current_user)):
    tasks_query = db.query(models.Task).filter(models.Task.id == id)

    task = tasks_query.first()

    if  not tasks_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="page not found")
    
    if task.user_id != int(get_current_user.id):
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="invalid request for this credential")
    
    tasks_query.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT )


@router.put("/{id}")                                                #id = task_id
def update_task(id:int, updated_task:schema.task, db : Session = Depends(database.get_db),get_current_user = Depends(oauth2.get_current_user)):
    tasks_query = db.query(models.Task).filter(models.Task.id == id)

    tasks = tasks_query.first()
    
    if  not tasks_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="page not found")
    
    if tasks.user_id != int(get_current_user.id):
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="invalid request for this credential")
    
    tasks_query.update(updated_task.dict())
    db.commit()
    return tasks_query.first()
    