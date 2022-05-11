from django import forms
from .models import App


class AddAppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ('app_name', 'description')

        widgtes = {
            'app_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }