from abc import ABC, abstractmethod

class ChatRepository(ABC):

    @abstractmethod
    def create(self, request):
        raise NotImplementedError

    @abstractmethod
    def get_user_chats(self, user_id):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id):
        raise NotImplementedError

    @abstractmethod
    def update(self, id):
        raise NotImplementedError