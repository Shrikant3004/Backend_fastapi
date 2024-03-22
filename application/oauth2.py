from jose import JWTError,jwt   
from datetime import datetime,timedelta
from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from . import schema
from .config import settings

secret_key = settings.secret_key
Algorithm  = settings.algorithm


oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")  # for request to "/login"  tokenUrl = "login"

def create_access_token(data : dict):
    to_encode = data.copy()
    token  = jwt.encode(to_encode,secret_key,algorithm=Algorithm)

    return token


def verify_access_token(token:str,credential_exception):  #token is taken input in this function from postman
  try: 
   payload = jwt.decode(token,secret_key,algorithms=[Algorithm])
   id:str = payload.get("user_id")
   if not id:
       raise credential_exception
   token_data = schema.tokendata(id=id)
  except JWTError:
    raise credential_exception
  return token_data   


def get_current_user(token:str=Depends(oauth2_schema)):
   credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid credential")

   return   verify_access_token(token,credential_exception)