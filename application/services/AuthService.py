from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import infrastructure.security.AccessTokenManager as tk
from infrastructure.security import AccessTokenManager
from domain.exceptions.exceptions import credentials_exception
from domain.repository.UserRepository import UserRepository
from domain.repository.HashRepository import HashRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

class AuthService:

    def get_current_user(token: str = Depends(oauth2_scheme) ):  

        return tk.verify_token(token, credentials_exception)
    
    def get_user_access_token(request, userRepository: UserRepository, hashRepository: HashRepository, accessTokenManager: AccessTokenManager):
        user = userRepository.get_by_email(request.username)
        
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        if not hashRepository.verify(request.password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
        
        access_token = tk.create_access_token(data={"sub": user.email})
        return access_token