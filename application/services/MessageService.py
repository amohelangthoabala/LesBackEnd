from domain.repository.MessageRepository import MessageRepository
from domain.repository.ChatRepository import ChatRepository
from domain.repository.UserRepository import UserRepository
from infrastructure.schemas.schemas import Message, CreateMessage
# from domain.models import message
from fastapi import Response, HTTPException, status

class MessageServices:

    def create_message(request: CreateMessage, messageRepository: MessageRepository, chatRepository: ChatRepository, userRepository: UserRepository):
        # chatRepository.create({intiator_id: request.sender, target_id: request.target})
        # return messageRepository.create(request)
        initiator = userRepository.get_by_email(request.sender.email)
        target = userRepository.get_by_email(request.target.email)
        
        chat = chatRepository.get_chat(initiator.id, target.id)
        
        if chat:
            print(chat.id)
            
        else:
            print(0)

    def get_by_id(id, messageRepository: MessageRepository):
        return messageRepository.get_by_id(id)
