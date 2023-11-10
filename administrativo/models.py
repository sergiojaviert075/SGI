from django.db import models
from core.helper_model import ModeloBase
from core.core import IDENTIFICACIONES
from baseapp.models import Persona, Genero
from core.core import CATEGORIAS, ESTADOS_PRINCIPALES

class DatosOrganizacion(ModeloBase):
    nombre = models.CharField(blank=True, null=True, max_length=500, verbose_name=u"Nombre de la empresa")
    direccion = models.CharField(blank=True, null=True, max_length=500, verbose_name=u"Dirección de la empresa")
    latitud = models.FloatField(default=0, blank=True, null=True, verbose_name="Latitud")
    longitud = models.FloatField(default=0, blank=True, null=True, verbose_name="Longitud")
    radio = models.FloatField(default=0, blank=True, null=True, verbose_name="Radio disponible para marcar")

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ['id']

    def __str__(self):
        return f"{self.nombre}"

class PersonaPerfil(ModeloBase):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True)
    is_administrador_principal = models.BooleanField(default=False, verbose_name=u'Es administrador principal?')
    is_administrador = models.BooleanField(default=False, verbose_name=u'Es administrador?')
    is_agente = models.BooleanField(default=False, verbose_name=u'Es agente?')
    is_usuariofinal = models.BooleanField(default=False, verbose_name=u'Es usuario final?')

    class Meta:
        verbose_name = "Perfil de persona"
        verbose_name_plural = "Perfiles de personas"
        ordering = ['id']

    def nombre_persona(self):
        return self.persona.__str__()

    def __str__(self):
        if self.es_administrador() and self.es_usuariofinal() and self.es_agente():
            return u'%s - %s' % (self.nombre_persona(), "ADMINISTRADOR - USUARIO - AGENTE")

        elif self.es_administrador() and self.es_agente() and not self.es_usuariofinal():
            return u'%s - %s' % (self.nombre_persona(), "ADMINISTRADOR - AGENTE")
        elif self.es_administrador() and self.es_usuariofinal() and not self.es_agente():
            return u'%s - %s' % (self.nombre_persona(), "ADMINISTRADOR - USUARIO")
        elif not self.es_administrador() and self.es_usuariofinal() and self.es_agente():
            return u'%s - %s' % (self.nombre_persona(), "AGENTE - USUARIO")

        elif not self.es_administrador() and not self.es_agente() and self.es_usuariofinal():
            return u'%s - %s' % (self.nombre_persona(), "USUARIO")
        elif self.es_administrador() and not self.es_usuariofinal() and not self.es_agente():
            return u'%s - %s' % (self.nombre_persona(), "ADMINISTRADOR")
        elif not self.es_administrador() and not self.es_usuariofinal() and self.es_agente():
            return u'%s - %s' % (self.nombre_persona(), "AGENTE")
        else:
            return u'%s - %s' % (self.nombre_persona(), "NO TIENE PERFIL")

    def get_perfil(self):
        if self.es_administrador() and self.es_usuariofinal() and self.es_agente():
            return u'%s' % ("ADMINISTRADOR - USUARIO - AGENTE")

        elif self.es_administrador() and self.es_agente() and not self.es_usuariofinal():
            return u'%s' % ("ADMINISTRADOR - AGENTE")
        elif self.es_administrador() and self.es_usuariofinal() and not self.es_agente():
            return u'%s' % ("ADMINISTRADOR - USUARIO")
        elif not self.es_administrador() and self.es_usuariofinal() and self.es_agente():
            return u'%s' % ("AGENTE - USUARIO")

        elif not self.es_administrador() and not self.es_agente() and self.es_usuariofinal():
            return u'%s' % ("USUARIO")
        elif self.es_administrador() and not self.es_usuariofinal() and not self.es_agente():
            return u'%s' % ("ADMINISTRADOR")
        elif not self.es_administrador() and not self.es_usuariofinal() and self.es_agente():
            return u'%s' % ("AGENTE")
        else:
            return u'%s' % "NO TIENE PERFIL"


    def es_usuariofinal(self):
        return self.is_usuariofinal

    def es_agente(self):
        return self.is_agente

    def es_administrador(self):
        return self.is_administrador


class Incidencia(ModeloBase):
    responsable = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True)
    titulo = models.CharField(max_length=800, blank=True, null=True)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    categoria = models.IntegerField(default=1, choices=CATEGORIAS)
    estado = models.IntegerField(default=1, choices=ESTADOS_PRINCIPALES)
    archivo = models.FileField(upload_to='archivoincidencia', blank=True, null=True, verbose_name='Evidencia de la incidencia')

    def __str__(self):
        return self.titulo
