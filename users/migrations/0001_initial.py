# Generated by Django 4.2.8 on 2023-12-04 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chats', '0002_alter_channel_moderators_alter_groupchat_moderators'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('channels', models.ManyToManyField(related_name='users', to='chats.channel')),
                ('direct_chats', models.ManyToManyField(related_name='users', to='chats.directchat')),
                ('group_chats', models.ManyToManyField(related_name='users', to='chats.groupchat')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
