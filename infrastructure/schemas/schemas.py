from pydantic import BaseModel
from typing import List, Optional
from jose import JWTError, jwt

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
    created_date: str

    sender: User

class Chat(BaseModel):

    messages = List[Message]
