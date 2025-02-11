from .models import Comment
from django import forms

# Create a form for the Comment model
# This form will be used to create a new comment
# It will be displayed in the post_detail view

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('title','level','rating','platinum_achieved','platinum_stability','glitched_trophies','glitched_trophies_list','game_version','playtime','platform','body',)