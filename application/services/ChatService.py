from domain.repository.ChatRepository import ChatRepository
from infrastructure.schemas.schemas import Chat
from fastapi import Response, HTTPException, status

class ChatServices:

    def create_chat(request, chatRepository: ChatRepository):
        return chatRepository.create(request)

    def get_by_id(id, chatRepository: ChatRepository):
        return chatRepository.get_by_id(id)