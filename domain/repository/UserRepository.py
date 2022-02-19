from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    def create(self, request):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    def get_by_email(self, email):
        raise NotImplementedError

    
    @abstractmethod
    def delete(self, id):
        raise NotImplementedError

    @abstractmethod
    def update(self, id):
        raise NotImplementedError

    
