from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#silka na bazu
# SQLALCHEMY_DATABASE_URL = 'sqlite:///data.db'
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@database/postgres'


#podklyucheniya k baze
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#generatsiya sessiyi
SessionLocal = sessionmaker(bind=engine)

#obshiy klass dlya moduley(models.py)
Base = declarative_base()

#import moduley
from database import models

#funksiya dlya generatsiyi svyazey k baze dannix
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()