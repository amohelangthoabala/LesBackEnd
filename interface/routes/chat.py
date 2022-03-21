from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
import application.usecases.oauth2 as auth
from application.services.ChatService import ChatServices
from infrastructure.repository.SQLAlchemy.ChatRepository import ChatRepositoryImpl as cri
from infrastructure.schemas import schemas
from infrastructure.database import database 
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/chat",
    tags=["Chats"]
)

get_db = database.get_db

@router.post('/')
def create_chat(request: schemas.ChatRequest, db: Session = Depends(get_db)):
    chatRepository = cri(db)

    return ChatServices.create_chat(request, chatRepository)

@router.get('/{id}', response_model=schemas.Chat)
def get_by_id(id: int, db: Session = Depends(get_db)):
    chatRepository = cri(db)

    return ChatServices.get_by_id(id, chatRepository)
    
