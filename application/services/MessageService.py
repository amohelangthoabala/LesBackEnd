from domain.repository.MessageRepository import MessageRepository
from infrastructure.schemas.schemas import Message
# from domain.models import message
from fastapi import Response, HTTPException, status

class MessageServices:

    def create_message(request: Message, messageRepository: MessageRepository):
        return messageRepository.create(request)

    def get_by_id(id, messageRepository: MessageRepository):
        return messageRepository.get_by_id(id)
