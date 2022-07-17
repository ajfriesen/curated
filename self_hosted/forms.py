from django import forms
from .models import App


class AddAppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ('app_name', 'description', "github_url", "svg_logo" )

        widgtes = {
            'app_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control'}),
            'svg_logo': forms.FileInput(attrs={'class': 'form-control'}),
        }