from django.db import models
from chats.models import GroupChat, DirectChat, Channel
from django.contrib.auth.models import User
from chats.models import Chat

from project import settings


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="messages")
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    # сделать не только текст но и видео, картинки и тд
    is_sent = models.BooleanField(default=False)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)


# class Message(models.Model):
#     sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="messages")
#     timestamp = models.DateTimeField(auto_now_add=True)
#     content = models.TextField()
#     # сделать не только текст но и видео, картинки и тд
#     is_sent = models.BooleanField(default=False)

#
# class DirectMessage(Message):
#     direct_chat = models.ForeignKey(DirectChat, on_delete=models.CASCADE, related_name='messages')
#     # Логика отправки сообщения
#     # ...
#     # После отправки сообщения устанавливаем атрибут is_sent в True и сохраняем изменеия!
#     # is_sent = True
#     # self.save()
#
#
# class GroupMessage(Message):
#     group_chat = models.ForeignKey(GroupChat, on_delete=models.CASCADE, related_name='messages')
#
#     # Логика отправки сообщения
#     # ...
#     # После отправки сообщения устанавливаем атрибут is_sent в True и сохраняем изменеия!
#     # is_sent = True
#     # self.save()
#
#
# class ChannelMessage(Message):
#     channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='messages')
#     # Логика отправки сообщения
#     # ...
#     # После отправки сообщения устанавливаем атрибут is_sent в True и сохраняем изменеия!
#     # is_sent = True
#     # self.save()
