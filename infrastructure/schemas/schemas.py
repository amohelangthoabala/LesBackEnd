from pydantic import BaseModel
from typing import List, Optional
from jose import JWTError, jwt
from datetime import datetime

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    # blogs: List[Blog] = []

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class Message(BaseModel):

    message: str
    status: str
    created_date: Optional[datetime]
    # chat_id: int
    # sender_id: int

    class Config():
        orm_mode = True


class Chat(BaseModel):

    initiator: ShowUser
    target: ShowUser
    messages = List[Message]

    class Config():
        orm_mode = True

class ChatRequest(BaseModel):

    initiator_id: int
    target_id: int

class CreateMessage(BaseModel):
    message: str
    status: str
    chat: Chat
    sender: ShowUser
    