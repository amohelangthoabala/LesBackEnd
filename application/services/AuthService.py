from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import infrastructure.security.AccessTokenManager as tk
from domain.exceptions.exceptions import credentials_exception

class AuthService:

    def get_current_user(token: str = Depends(oauth2_scheme) ):  

        return tk.verify_token(token, credentials_exception)