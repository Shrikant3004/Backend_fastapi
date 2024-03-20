from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy import Column,String,Integer,Boolean,TIMESTAMP,ForeignKey
from sqlalchemy.orm import relationship





class User(Base):
    __tablename__ = "Users_project"

    id = Column(Integer,nullable=False,primary_key = True)
    username = Column(String,nullable = False,unique=True)
    password = Column(String,nullable = False)
    created_at = Column(TIMESTAMP(timezone=True),nullable = False, server_default = text('now()'))