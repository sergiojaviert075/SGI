from django.urls import path

from administrativo.view_personas import listar_personas, crear_persona, editar_persona, eliminar_persona, activar_desactivar_perfil,\
    resetear_clave
from administrativo.view_misincidencias import *
from administrativo.view_gestionincidencias import *
from administrativo.views import *

app_name = 'administrativo'
urlpatterns = [

    #CONSULTAS AUTOEJECUTABLES
    path('/consultaAdministrativos/', consultaAdministrativos, name='consultaAdministrativos'),
    path('/consultaIncidencias/', consultaIncidencias, name='consultaIncidencias'),
    path('/consultaPersonas/', consultaPersonas, name='consultaPersonas'),
    path('/consultaModulos/', consultaModulos, name='consultaModulos'),

    #MÓDULO PERSONAS
    path('personas/', listar_personas, name='listar_personas'),
    path('personas/add', crear_persona, name='crear_persona'),
    path('personas/eliminar/', eliminar_persona, name='eliminar_persona'),
    path('personas/editar/<int:pk>/', editar_persona, name='editar_persona'),
    path('personas/activar_desactivar_perfil/', activar_desactivar_perfil, name='activar_desactivar_perfil'),
    path('personas/resetear_clave/', resetear_clave, name='resetear_clave'),

    #MÓDULO MIS INCIDENCIAS
    path('misincidencias/', listar_misincidencias, name='listar_misincidencias'),
    path('misincidencias/add', crear_miincidencia, name='crear_miincidencia'),
    path('misincidencias/eliminar/', eliminar_miincidencia, name='eliminar_miincidencia'),
    path('misincidencias/editar/<int:pk>/', editar_miincidencia, name='editar_miincidencia'),

    #MÓDULO GESTIÓN DE INCIDENCIAS
    path('gestionincidencias/', listar_incidencias, name='listar_incidencias'),
]
