from abc import ABC, abstractmethod

class MessageRepository(ABC):

    @abstractmethod
    def create(self, request):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    def search(self, id, keyword):
        raise NotImplementedError

    @abstractmethod
    def update(self, id, request):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id):
        raise NotImplementedError