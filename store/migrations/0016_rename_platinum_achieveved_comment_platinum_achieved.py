# Generated by Django 4.2.18 on 2025-02-05 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_post_technical_vrr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='platinum_achieveved',
            new_name='platinum_achieved',
        ),
    ]
