from django.contrib import admin
from .models import Game, Profile
# from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


# @admin.register(Profile)
# class ProfileAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content',)

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.

class AccountInLine(admin.StackedInline):
    model = Game
    can_delete = True
    extra = 0 # how many extra fields to display
    verbose_name_plural = 'games_purchased'

class CustomizedUserAdmin (AuthUserAdmin):
    inlines = (AccountInLine,)


class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('purchased_games',)

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Profile, ProfileAdmin)