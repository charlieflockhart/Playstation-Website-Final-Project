from django.contrib import admin
from .models import Game
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
    can_delete = False
    extra = 1 # how many extra fields to display
    verbose_name_plural = 'games_purchased'

class CustomizedUserAdmin (AuthUserAdmin):
    inlines = (AccountInLine,)

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)