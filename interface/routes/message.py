from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
import application.usecases.oauth2 as auth
from application.services.MessageService import MessageServices
from infrastructure.repository.SQLAlchemy.MessageRepository import MessageRepositoryImpl as mri
from infrastructure.schemas import schemas
from infrastructure.database import database 
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/message",
    tags=["Messages"]
)

get_db = database.get_db

@router.post('/', response_model= schemas.Message)
def create_message(request: schemas.Message, db: Session = Depends(get_db)):
    messageRepository = mri(db)

    return MessageServices.create_message(request, messageRepository)

@router.get('/{id}')
def get_by_id(id: int, db: Session = Depends(get_db)):
    messageRepository = mri(db)

    return MessageServices.get_by_id(id, messageRepository)
    
