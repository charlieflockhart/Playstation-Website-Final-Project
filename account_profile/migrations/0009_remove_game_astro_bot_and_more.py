# Generated by Django 4.2.18 on 2025-02-10 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_alter_comment_title'),
        ('account_profile', '0008_game_astro_bot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='Astro_Bot',
        ),
        migrations.RemoveField(
            model_name='game',
            name='Grand_Theft_Auto_VI',
        ),
        migrations.AddField(
            model_name='profile',
            name='purchased_games',
            field=models.ManyToManyField(blank=True, null=True, related_name='purchased_games', to='store.post'),
        ),
    ]
