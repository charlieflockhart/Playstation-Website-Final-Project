from django.contrib.auth.models import User
from django.db import models 
from cloudinary.models import CloudinaryField
from store.models import Post


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchased_games = models.ManyToManyField(Post, related_name='purchased_games', blank=True)

    def __str__(self):
        return self.user.username
    
class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.games_purchased