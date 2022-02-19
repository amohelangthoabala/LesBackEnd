from abc import ABC, abstractmethod

class HashRepository(ABC):

    @abstractmethod
    def encrypt(self, password: str):
        raise NotImplementedError

    @abstractmethod
    def verify(self, plain_password: str, hashed_password: str):
        raise NotImplementedError