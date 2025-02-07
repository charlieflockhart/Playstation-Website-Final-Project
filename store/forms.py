from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('title','level','rating','platinum_achieved','platinum_stability','glitched_trophies','glitched_trophies_list','game_version','playtime','platform','body',)

# class SearchForm(forms.ModelForm):
#     query = forms.CharField(label="Search", max_length=100)