from fastapi import FastAPI
from . routers import users
from . import models
from . database import engine

models.Base.metadata.create_all(bind = engine)  #creates the table

app = FastAPI()
app.include_router(users.router)  #routing 

