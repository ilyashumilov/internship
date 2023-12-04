from django.db import models
from django.contrib.auth.models import User
from chats.models import GroupChat, DirectChat, Channel

from project import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=100)

    direct_chats = models.ManyToManyField(DirectChat, related_name="users")
    group_chats = models.ManyToManyField(GroupChat, related_name="users")
    channels = models.ManyToManyField(Channel, related_name="users")
