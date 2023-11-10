from django.urls import path

from administrativo.view_personas import listar_personas, crear_persona, editar_persona, eliminar_persona, activar_desactivar_perfil,\
    resetear_clave
from administrativo.view_mibiografia import mibiografia, datos_familiares, crear_datosfamiliares, editar_datosfamiliares, \
    eliminar_datosfamiliares, editar_mibiografia, mis_marcadas

app_name = 'administrativo'
urlpatterns = [
    #URLS CATEGORÍA ADMINISTRATIVO

    #MÓDULO PERSONAS
    path('personas/', listar_personas, name='listar_personas'),
    path('personas/add', crear_persona, name='crear_persona'),
    path('personas/eliminar/<int:pk>/', eliminar_persona, name='eliminar_persona'),
    path('personas/editar/<int:pk>/', editar_persona, name='editar_persona'),
    path('personas/activar_desactivar_perfil/', activar_desactivar_perfil, name='activar_desactivar_perfil'),
    path('personas/resetear_clave/', resetear_clave, name='resetear_clave'),

#MÓDULO MI BIOGRAFÍA
    path('mibiografia/', mibiografia, name='mibiografia'),
    path('mibiografia/editar/', editar_mibiografia, name='editar_mibiografia'),
    path('datos_familiares/', datos_familiares, name='datos_familiares'),
    path('datosfamiliares/add', crear_datosfamiliares, name='crear_datosfamiliares'),
    path('datosfamiliares/editar/<int:id>/', editar_datosfamiliares, name='editar_datosfamiliares'),
    path('datosfamiliares/eliminar/<int:id>/', eliminar_datosfamiliares, name='eliminar_datosfamiliares'),
    path('mis_marcadas/', mis_marcadas, name='mis_marcadas'),
]
