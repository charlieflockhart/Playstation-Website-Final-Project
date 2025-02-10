from django.contrib.auth.models import User
from django.db import models 
from store.models import Post
from django.db.models.signals import post_save
from django.dispatch import receiver

# Profile model for user profile page   
# This model is used to store the user's purchased games
# The user's purchased games are displayed on the user profile page
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userprofile')
    purchased_games = models.ManyToManyField(Post, related_name='purchased_games', blank=True)

    def __str__(self):
        return self.user.username

# Create or update the user profile
# This function creates or updates the user profile
# It is called when a user is created or updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Profile.objects.create(user=instance)