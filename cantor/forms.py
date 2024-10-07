from django import forms
from .models import Cantor

class CantorForm(forms.ModelForm):
    class Meta:
        model = Cantor
        fields = ['nome']