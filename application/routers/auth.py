from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database,models,hashing,schema,oauth2
router = APIRouter(tags=["login"])

@router.post("/login")
def login(user_credential:OAuth2PasswordRequestForm=Depends(), db:Session = Depends(database.get_db)):
   user = db.query(models.User).filter(models.User.username==user_credential.username).first()
   if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
   
   if not hashing.verify(user_credential.password,user.password):
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="wrong credential")
   
   access_token = oauth2.create_access_token(data={"user_id":user.id})
   new_token = schema.token(access_token=access_token,token_type="bearer")
   return new_token