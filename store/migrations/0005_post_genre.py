# Generated by Django 4.2.18 on 2025-02-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_post_game_platform_ps4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.TextField(default='Action, Adventure, RPG'),
        ),
    ]
