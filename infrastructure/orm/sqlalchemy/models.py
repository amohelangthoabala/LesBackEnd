import datetime
from infrastructure.database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    status = Column(String)
    password = Column(String)

    initiator = relationship("Chat", backref="Initiator", lazy="dynamic", foreign_keys="Chat.initiator_id")
    target = relationship("Chat", backref="Target", lazy="dynamic", foreign_keys="Chat.target_id")

    messages = relationship("Message", back_populates="sender")

class Chat(Base):
    __table__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    
    initiator_id = Column(Integer, ForeignKey('users.id'))
    target_id = Column(Integer, ForeignKey('users.id'))

    messages = relationship("Message", back_populates="chat")
    

class Message(Base):
    __table__ = "messages"

    id = Column(Integer, primary_key=True, index=True)

    message = Column(String)
    status = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    
    chat_id = Column(Integer, ForeignKey('chats.id'))
    sender_id = Column(Integer, ForeignKey('users.id'))

    sender = relationship("User", back_populates="messages")
    chat = relationship("Chat", back_populates="messages")

