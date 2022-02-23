from domain.repository.ChatRepository import ChatRepository
from sqlalchemy.orm import Session
from infrastructure.schemas import schemas
from infrastructure.orm.sqlalchemy import models

class ChatRepositoryImpl(ChatRepository):
    
    def __init__(self, db: Session):

        self.db = db
        self.chat = models.Chat

    def create(self, request):
        new_chat = self.chat(initiator_id=request.initiator_id, target_id=request.target_id)

        self.db.add(new_chat)
        self.db.commit()
        self.db.refresh(new_chat)

        return new_chat

    def get_by_id(self, id):
        return self.db.query(self.chat).filter(self.chat.id == id).first()

    def get_user_chats(self, user_id):
        pass
    
    def update(self, id, request):
        chat = self.db.query(self.chat).filter(self.chat.id == id).first()
        db.delete(message)
        db.commit()

        return chat

    def delete(self, id):
        chat = self.db.query(self.chat).filter(self.chat.id == id).first()
        db.delete(message)
        db.commit()

        return chat