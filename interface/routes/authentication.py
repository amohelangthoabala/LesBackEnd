from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from infrastructure.security import AccessTokenManager as token
from infrastructure.orm.sqlalchemy import models
from infrastructure.schemas import schemas
from infrastructure.database import database 
from sqlalchemy.orm import Session
from infrastructure.repository.SQLAlchemy.HashRepository import HashRepositoryImpl as hri
from infrastructure.repository.SQLAlchemy.UserRepository import UserRepositoryImpl as uri
from application.services.AuthService import AuthService

router = APIRouter(
    tags=['authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    
    userRepository = uri(db)
    hashRepository = hri()
    accessTokenManager = token
    
    access_token = AuthService.get_user_access_token(request, userRepository, hashRepository, accessTokenManager)
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post('/password-recovery/{email}')
def password_recovery(email: str, db:Session = Depends(database.get_db)):
    
    return {"Link send to your email": "Link"}

@router.post('/password-reset/')
def password_recovery(email: str, db:Session = Depends(database.get_db)):
    
    return {"OTP": "4345", "new password": "fndvdiuss", "confirm password": "fndvdiuss"}