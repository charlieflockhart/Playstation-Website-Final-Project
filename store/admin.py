from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# PostAdmin class to customize the admin panel
# This class will display the title, slug, status, and created_on fields in the admin panel
# It will also allow the admin to search for posts by title and game_info
# The admin can filter posts by status and created_on date
# The slug field will be prepopulated based on the title field
# The game_info field will use the Summernote editor for rich text editing

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'game_info']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('game_info',)

# Register your models here.
admin.site.register(Comment)
