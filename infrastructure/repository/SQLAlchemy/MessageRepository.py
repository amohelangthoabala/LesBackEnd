from domain.repository.MessageRepository import MessageRepository
from sqlalchemy.orm import Session
from infrastructure.schemas import schemas
from infrastructure.orm.sqlalchemy import models

class MessageRepositoryImpl(MessageRepository):

    def __init__(self, db: Session):

        self.db = db
        self.message = models.Message

    def create(self, request: schemas.Message):
        new_message = self.message(message=request.message, status=request.status, chat_id=1, sender_id=1)

        self.db.add(new_message)
        self.db.commit()
        self.db.refresh(new_message)

        return new_message

    def get_by_id(self, id):
        return self.db.query(self.message).filter(self.message.id == id).first()

    def search(self, id, keyword):
        messages = self.db.query(self.message).filter(self.message.message.like(keyword)).all()

    def update(self, id, request):
        message = self.db.query(self.message).filter(self.message.id == id).first()
        db.delete(message)
        db.commit()

        return message

    def delete(self, id):
        message = self.db.query(self.message).filter(self.message.id == id).first()
        db.delete(message)
        db.commit()

        return message