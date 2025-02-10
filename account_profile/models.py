from django.contrib.auth.models import User
from django.db import models 
from cloudinary.models import CloudinaryField
from store.models import Post
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userprofile')
    purchased_games = models.ManyToManyField(Post, related_name='purchased_games', blank=True)

    def __str__(self):
        return self.user.username
    
class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    games_purchased = models.TextField(default='')

    def __str__(self):
        return self.games_purchased
    

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Profile.objects.create(user=instance)
    # Existing users: just save the profile
    # instance.userprofile.save()