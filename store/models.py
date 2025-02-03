from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    developer = models.CharField(max_length=200, blank=True, default='Unknown')
    publisher = models.CharField(max_length=200, blank=True, default='Unknown')
    featured_image = CloudinaryField('image', default='placeholder')
    release_date = models.DateField(auto_now=False, auto_now_add=False, default='2021-01-01')
    game_version = models.DecimalField(max_digits=6, decimal_places=2 , default=0.00)
    price = models.DecimalField(max_digits=6, decimal_places=2 , default=0.00)
    playtime = models.IntegerField(default=0)
    age_rating = models.IntegerField(default=0)
    game_info = models.TextField(default='')
    # awards_shown = models.BooleanField(default=False)
    awards_won = models.TextField(default='No Awards Have Been Posted Here Yet..')
    genre = models.TextField(default='Action, Adventure, RPG')
    game_platform = models.TextField(default='PS_ PS_')
    technical_refresh_rate = models.IntegerField(default=60)
    technical_hdr = models.BooleanField(default=False)
    technical_storagesize = models.IntegerField(default=0)
    technical_online_play = models.BooleanField(default=False)
    technical_online_players = models.IntegerField(default=0)
    technical_online_crossplay = models.BooleanField(default=False)
    technical_monthly_concurrent_players = models.IntegerField(default=0)
    platinum_trophies = models.BooleanField(default=False)
    trophy_ammount = models.IntegerField(default=0)
    patch_notes = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"