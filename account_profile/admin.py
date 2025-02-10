from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

# Creates a new class that inherits from the ModelAdmin class
# This class allows for the purchased_games field to be displayed as a filter_horizontal field

class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('purchased_games',)

admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Profile, ProfileAdmin)