from .models import Chat


def create_new_chat() -> Chat:
    new_chat = Chat(chat_type='GroupChat')
    return new_chat.save()

