from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator

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
    awards_shown = models.BooleanField(default=False)
    awards_won = models.TextField(default='Award Name - "Best Game of the Year"\nAwarding Organization - "The Game Awards"\nYear of Award - "2025"\nCategory - "Best Action Game')
    genre = models.TextField(default='Action, Adventure, RPG')
    game_platform = models.TextField(default='PS_ PS_')
    technical_subtitles = models.BooleanField(default=False)
    technical_refresh_rate = models.IntegerField(default=60)
    technical_vrr = models.BooleanField(default=False)
    technical_ray_tracing = models.BooleanField(default=False)
    technical_hdr = models.BooleanField(default=False)
    technical_storagesize = models.IntegerField(default=0)
    technical_online_play = models.BooleanField(default=False)
    technical_online_players = models.IntegerField(default=0)
    technical_online_console_crossplay = models.BooleanField(default=False)
    technical_online_pc_crossplay = models.BooleanField(default=False)
    technical_monthly_concurrent_players = models.IntegerField(default=0)
    platinum_trophies = models.BooleanField(default=False)
    trophy_amount = models.IntegerField(default=0)
    trophy_achieved_percentage = models.FloatField(default=0.0)
    trophy_duration_to_plat = models.IntegerField(default=0)
    trophy_plat_difficulty = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    trophy_plat_glitchiness = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    patch_notes_url = models.URLField(default='https://store.playstation.com/en-gb/pages/latest')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    title = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    platinum_achieved = models.BooleanField(default=False)
    platinum_stability = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    glitched_trophies = models.BooleanField(default=False)
    glitched_trophies_list = models.TextField(default='No Glitched Trophies Have Been Posted Here Yet..')
    game_version = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    playtime = models.IntegerField(default=0)
    PLATFORM_CHOICES = [
        ('PS4', 'PlayStation 4'),
        ('PS5', 'PlayStation 5'),
    ]
    platform = models.CharField(max_length=3, choices=PLATFORM_CHOICES, default='PS4')
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"