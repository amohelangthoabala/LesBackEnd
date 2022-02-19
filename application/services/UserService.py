from domain.repository.UserRepository import UserRepository
from domain.repository.HashRepository import HashRepository
from domain.models import user
from fastapi import Response, HTTPException, status

class UserServices:
    
    def create_user(request: user, userRepository: UserRepository, hashRepository: HashRepository):
        user = userRepository.get_by_email(request.email)

        #check if user already exists
        if user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with email already exists")

        # hash user password
        request.password = hashRepository.encrypt(request.password)

        return userRepository.create(request)

        
    def get_user_by_id(id, userRepository: UserRepository):

        return userRepository.get_by_id(id)