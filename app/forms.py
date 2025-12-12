from django import forms
from .models import Coche

class CocheForm(forms.ModelForm):
    class Meta:
        model = Coche
        fields = ["titulo", "precio", "ubicacion", "descripcion", "imagen"]

        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-input"}),
            "precio": forms.NumberInput(attrs={"class": "form-input"}),
            "ubicacion": forms.TextInput(attrs={"class": "form-input"}),
            "descripcion": forms.Textarea(attrs={"class": "form-textarea"}),
        }
