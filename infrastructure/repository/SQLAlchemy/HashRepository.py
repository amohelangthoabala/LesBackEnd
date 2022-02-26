from passlib.context import CryptContext
from domain.repository.HashRepository import HashRepository

class HashRepositoryImpl(HashRepository):

    def __init__(self):
        self.pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def encrypt(self, password:str):
        return self.pwd_cxt.hash(password)

    def verify(self, plain_password: str, hashed_password: str):
        return self.pwd_cxt.verify(plain_password, hashed_password)
