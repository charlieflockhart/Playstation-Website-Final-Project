# Generated by Django 4.2.18 on 2025-02-10 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account_profile', '0010_alter_profile_purchased_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='content',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='title',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='updated_on',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
