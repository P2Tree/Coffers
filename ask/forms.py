from django import forms
from .models import Ask

class AskForm(forms.ModelForm):

    class Meta:
        model = Ask

        fields = ['question']
