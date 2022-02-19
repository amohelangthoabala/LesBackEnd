from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
import application.usecases.oauth2 as auth
from application.services.UserService import UserServices
# from infrastructure.repository import UserRepository as ur
from infrastructure.repository.SQLAlchemy.UserRepository import UserRepositoryImpl as uri
from infrastructure.repository.SQLAlchemy.HashRepository import HashRepositoryImpl as hri
from infrastructure.schemas import schemas
from infrastructure.database import database 
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

get_db = database.get_db

@router.post("/", response_model = schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    userRepository = uri(db)
    hashRepository = hri()
    return UserServices.create_user(request, userRepository, hashRepository)
    # return ur.create_user(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    userRepository = uri(db)
    return UserServices.get_user_by_id(id, userRepository)
    # return ur.get_user(id, db)
