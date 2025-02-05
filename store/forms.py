from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('level','rating','platinum_achieved','platinum_stability','glitched_trophies','glitched_trophies_list','game_version','playtime','platform','body',)