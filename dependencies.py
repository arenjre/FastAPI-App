from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

def db_dependency():
    return Depends(get_db)
