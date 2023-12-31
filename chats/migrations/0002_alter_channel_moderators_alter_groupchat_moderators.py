# Generated by Django 4.2.8 on 2023-12-04 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='moderators',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='channel_moderators', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='groupchat',
            name='moderators',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='group_chat_moderators', to='auth.group'),
        ),
    ]
