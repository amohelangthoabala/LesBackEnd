from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
import application.usecases.oauth2 as auth
from application.services.MessageService import MessageServices
from infrastructure.repository.SQLAlchemy.MessageRepository import MessageRepositoryImpl as mri
from infrastructure.repository.SQLAlchemy.ChatRepository import ChatRepositoryImpl as cri
from infrastructure.repository.SQLAlchemy.UserRepository import UserRepositoryImpl as uri
from infrastructure.schemas import schemas
from infrastructure.database import database 
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/message",
    tags=["Messages"]
)

get_db = database.get_db

@router.post('/', response_model= schemas.Message)
def create_message(request: schemas.CreateMessage, db: Session = Depends(get_db)):
    messageRepository = mri(db)
    chatRepository = cri(db)
    userRepository = uri(db)

    return MessageServices.create_message(request, messageRepository, chatRepository, userRepository)

@router.get('/{id}')
def get_by_id(id: int, db: Session = Depends(get_db)):
    messageRepository = mri(db)

    return MessageServices.get_by_id(id, messageRepository)
    
@router.get('/email')
def get_messages_owned_by_user(email):
    
    return {"email": email}