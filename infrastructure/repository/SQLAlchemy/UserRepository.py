from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from infrastructure.schemas import schemas
from infrastructure.orm.sqlalchemy import models
# from infrastructure.repository.SQLAlchemy.HashRepository import HashRepositoryImpl as Hash

from domain.repository.UserRepository import UserRepository

class UserRepositoryImpl(UserRepository):

    def __init__(self, db: Session):

        self.db = db
        self.user = models.User

    def create(self, request: schemas.User):
        new_user = self.user(name=request.name, email=request.email, password=request.password)#, password=Hash.encrypt(request.password))
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_by_id(self, id):
        return self.db.query(models.User).filter(self.user.id == id).first()

    def get_by_email(self, email):
        return self.db.query(models.User).filter(self.user.email == email).first()

    def delete(self, id):
        user = db.query(models.User).filter(self.user.id == id).first()
        db.session.delete(user)
        db.session.commit()

        return user

    def update(self, id, request):
        pass

def create_user(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details="User not found")

    return user