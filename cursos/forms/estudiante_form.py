from django import forms
from ..models import Estudiante


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ["nombre", "email", "avatar"]
        labels = {
            "nombre": "Nombre",
            "email": "Correo Electrónico",
            "avatar": "Avatar",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
