from pydantic import BaseModel
from datetime import datetime
from typing import List
class User(BaseModel):
    username : str
    password : str



class task(BaseModel):
    task : str
    user_id : int


class User_response(BaseModel):
    username : str
    created_at :datetime
    class Config:
        orm_mode = True

class task_response(BaseModel):
    user : User_response
    task : List[str]
    class Config:
        orm_mode = True