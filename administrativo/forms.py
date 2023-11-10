from django import forms
from core.core import CATEGORIAS, ESTADOS_PRINCIPALES

def no_requerido(form, campo):
    form.fields[campo].widget.required = False

def deshabilitar(form, campo):
    form.fields[campo].widget.attrs['disabled'] = True

class IncidenciaForm(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'u-full-width', 'required': 'True', 'label': 'Título'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'u-full-width', 'required': 'True', 'label': 'Descripción'}))
    categoria = forms.ChoiceField(choices=CATEGORIAS, label=u'Categoría', required=True, widget=forms.Select(attrs={'class': 'u-full-width', 'label': 'Categoría'}))
    archivo = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'u-full-width', 'label': 'Archivo', 'norequired': 'True', 'required': False}),)
