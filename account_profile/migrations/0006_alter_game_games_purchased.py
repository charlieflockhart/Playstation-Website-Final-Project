# Generated by Django 4.2.18 on 2025-02-08 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0005_alter_game_games_purchased'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='games_purchased',
            field=models.TextField(),
        ),
    ]
