from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from project import settings


class DirectChat(models.Model):
    name = models.CharField(max_length=100)
    members = models.OneToOneField(Group, on_delete=models.CASCADE, related_name="direct_chat_members")
    #нужны админы?


class GroupChat(models.Model):
    name = models.CharField(max_length=100)
    members = models.OneToOneField(Group, on_delete=models.CASCADE, related_name="group_chat_members") #теперь нужно?
    moderators = models.OneToOneField(Group, on_delete=models.CASCADE, related_name="group_chat_moderators")
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="own_chats") #сделать при удалении админа чтобы админом становился один из модеров


class Channel(models.Model):
    name = models.CharField(max_length=100)
    members = models.OneToOneField(Group, on_delete=models.CASCADE, related_name="channel_members")
    moderators = models.OneToOneField(Group, on_delete=models.CASCADE, related_name="channel_moderators")
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="own_channels") #сделать при удалении админа чтобы админом становился один из модеров


#сделать удаление групп при отсутствии участников или при удалении чата

ROLES_CHOISES = [
    ("GeneralMember", "GeneralMember"),
    ("Admin", "Admin"),
    ("Moderator", "Moderator"),
]

CHAT_TYPE_CHOISES = [
    ("DirectChat", "GeneralMember"),
    ("GroupChat", "GroupChat"),
    ("Channel", "Channel"),
]


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    # avatart  ....


class Chat(models.Model):
    chat_type = models.CharField(choices=CHAT_TYPE_CHOISES)


class ChatMemeber(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user")
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="chat")
    role = models.CharField(choices=ROLES_CHOISES)
