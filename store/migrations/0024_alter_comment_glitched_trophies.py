# Generated by Django 4.2.18 on 2025-02-10 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_alter_comment_approved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='glitched_trophies',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
