from fastapi import Depends,status,HTTPException,APIRouter
from fastapi.params import Body
from .. import schema,models,database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["users"]
) 


@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schema.User_response)
def Create_user(user:schema.User,db : Session = Depends(database.get_db),):
   


    new_user = models.User(**(user.dict()))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user