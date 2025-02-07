from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
    
class SupportRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(default='')
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Support request from {self.name}"   