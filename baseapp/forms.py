from django import forms
from core.helper_form import FormBase
from baseapp.models import Persona, Genero

class PersonaForm(forms.Form):
    nombres = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width', 'required': 'true'})
    )
    apellido1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width', 'required': 'true'})
    )
    apellido2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width', 'required': 'true'})
    )
    cedula = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width'})
    )
    pasaporte = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width'})
    )
    ruc = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width'})
    )
    direccion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width', 'required': 'true'})
    )
    genero = forms.ModelChoiceField(
        queryset=Genero.objects.filter(status=True),
        widget=forms.Select(attrs={'class': 'u-full-width'}),
    )
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'u-full-width', 'type': 'date', 'required': 'true'})
    )
    correo_electronico = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'u-full-width'})
    )
    telefono = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width'})
    )
    foto = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'u-full-width'}),
    )

