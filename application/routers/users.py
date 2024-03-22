from fastapi import Depends,status,HTTPException,APIRouter
from fastapi.params import Body
from .. import schema,models,database,hashing
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["users"]
) 


@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schema.User_response)
def Create_user(user:schema.User,db : Session = Depends(database.get_db),):
    same_username = db.query(models.User).filter(models.User.username == user.username).first()
    if same_username is not None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="username already taken")
    user.password = hashing.hash(user.password)

    new_user = models.User(**(user.dict()))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user