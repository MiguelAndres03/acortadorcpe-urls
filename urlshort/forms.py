from .models import ShortURL
from django import forms

class CreateNewShortURL(forms.ModelForm):
    class Meta:
        model=ShortURL
        fields = {'original_url', 'description','short_url'}

        widgets = {
            'original_url': forms.TextInput(attrs={'class': 'form-control','type': 'url', 'placeholder': 'Ingrese la URL original'}),
            'short_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la URL corta (Ej: Audiencia)'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese una descripción'})
        }

