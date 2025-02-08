from .models import Game
from django import forms


class PurchasedForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('games_purchased',)

# class SearchForm(forms.ModelForm):
#     query = forms.CharField(label="Search", max_length=100)