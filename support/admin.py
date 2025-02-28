from django.contrib import admin
from .models import SupportRequest
from django_summernote.admin import SummernoteModelAdmin

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.

@admin.register(SupportRequest)
class SupportRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)
    list_filter = ('read', 'issue_type',)