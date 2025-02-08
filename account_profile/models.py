from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    games_purchased = models.TextField(default='')