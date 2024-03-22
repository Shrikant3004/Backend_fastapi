from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

password = settings.database_password
host = settings.database_hostname
username = settings.database_username
database_name = settings.database_name

SQLALCHEMY_DATABASE_URL = 'postgresql://%s:%s@%s/%s'%(username,password,host,database_name)     #'postgresql://<username>:<password>@<ip-address/hostname>/database_name'
engine = create_engine(SQLALCHEMY_DATABASE_URL) 

Sessionlocal =sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

#dependencies
def get_db():
     db = Sessionlocal()
     try:
         yield db
     finally:
         db.close()    