from django.contrib import admin

from chats.models import GroupChat, DirectChat, Channel
from social.models import DirectMessage, GroupMessage, ChannelMessage
from users.models import UserProfile


@admin.register(UserProfile)
class GroupChat(admin.ModelAdmin):
    pass


@admin.register(GroupChat)
class GroupChat(admin.ModelAdmin):
    pass


@admin.register(DirectChat)
class DirectChat(admin.ModelAdmin):
    pass


@admin.register(Channel)
class Channel(admin.ModelAdmin):
    pass


@admin.register(DirectMessage)
class DirectMessage(admin.ModelAdmin):
    pass


@admin.register(GroupMessage)
class GroupMessage(admin.ModelAdmin):
    pass


@admin.register(ChannelMessage)
class ChannelMessage(admin.ModelAdmin):
    pass

#разделить талицы по админкам