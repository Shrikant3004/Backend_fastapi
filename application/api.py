from fastapi import FastAPI
from . routers import users,tasks,auth
from . import models
from . database import engine

models.Base.metadata.create_all(bind = engine)  #creates the table

app = FastAPI()
app.include_router(users.router)
app.include_router(tasks.router)  #routing
app.include_router(auth.router)  

