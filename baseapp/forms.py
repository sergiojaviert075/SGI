from django import forms
from core.helper_form import FormBase
from baseapp.models import Persona, Genero

def no_requerido(form, campo):
    form.fields[campo].widget.required = False

def deshabilitar(form, campo):
    form.fields[campo].widget.attrs['disabled'] = True

class PersonaForm(forms.Form):
    nombres = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width', 'required': 'True', 'label': 'Nombres'})
    )
    apellido1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width', 'required': 'True', 'label': 'Primer apellido'})
    )
    apellido2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width', 'required': 'True', 'label': 'Segundo apellido'})
    )
    cedula = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width', 'norequired': 'True', 'required': False, 'label': 'Cédula'})
    )
    pasaporte = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width', 'norequired': 'True', 'required': False, 'label': 'Pasaporte'})
    )
    ruc = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width', 'norequired': 'True', 'required': False, 'label': 'Ruc'})
    )
    direccion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width', 'required': 'True', 'label': 'Dirección'})
    )
    genero = forms.ModelChoiceField(
        queryset=Genero.objects.filter(status=True),
        widget=forms.Select(attrs={'class': 'u-full-width', 'label': 'Género', 'required': 'True'}),
    )
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'u-full-width', 'type': 'date', 'required': 'True', 'label': 'Fec. Nacimiento'})
    )
    correo_electronico = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'u-full-width', 'label': 'Email', 'norequired': 'True', 'required': False})
    )
    telefono = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'u-full-width', 'label': 'Teléfono', 'norequired': 'True', 'required': False})
    )
    foto = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'u-full-width', 'label': 'Foto', 'norequired': 'True', 'required': False}),
    )

    def no_requerir(self):
        no_requerido(self, 'cedula')
        no_requerido(self, 'pasaporte')
        no_requerido(self, 'ruc')
        no_requerido(self, 'correo_electronico')
        no_requerido(self, 'telefono')
        no_requerido(self, 'foto')

    def no_necesarios(self):
        deshabilitar(self, 'nombres')
        deshabilitar(self, 'apellido1')
        deshabilitar(self, 'apellido2')
        deshabilitar(self, 'cedula')
        deshabilitar(self, 'pasaporte')
        deshabilitar(self, 'ruc')

