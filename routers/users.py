from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
import config.oauth2 as auth
from repository import UserRepository as ur
from schemas import schemas
from config import database 
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

get_db = database.get_db

@router.post("/", response_model = schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):

   return ur.create_user(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    return ur.get_user(id, db)
