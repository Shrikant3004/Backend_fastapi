from pydantic import BaseModel
from datetime import datetime
from typing import List,Any,Optional
class User(BaseModel):
    username : str
    password : str



class task(BaseModel):
    task : str
    status : Optional[str]



class User_response(BaseModel):
    id : int
    username : str
    created_at :datetime
    class Config:
        orm_mode = True

class task_response(BaseModel):
    user : User_response
    task_info : List[Any]
    class Config:
        orm_mode = True

class token(BaseModel):
    access_token :str
    token_type :str
    class Config:
        orm_mode = True


class tokendata(BaseModel):
    id :str        