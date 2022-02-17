from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from config import JWTtoken as token
import models
from schemas import schemas
from config import database 
from sqlalchemy.orm import Session
from config.hashing import Hash

router = APIRouter(
    tags=['authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Imcorrect password")

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}