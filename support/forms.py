from .models import SupportRequest
from django import forms


class SupportRequestForm(forms.ModelForm):
    class Meta:
        model = SupportRequest
        fields = ('name', 'email', 'issue_type',  'message')