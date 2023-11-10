from django.urls import path

from system import views

app_name = 'sistema'
urlpatterns = [
    #
    path('modulos/', views.listar_modulo, name='listar_modulo'),
    path('modulos/add', views.crear_modulo, name='crear_modulo'),
    path('modulos/eliminar/<int:pk>/', views.eliminar_modulo, name='eliminar_modulo'),
    path('modulos/editar/<int:pk>/', views.editar_modulo, name='editar_modulo'),
    #
    path('modulos/categoria/', views.listar_categoria_modulo, name='listar_categoria_modulo'),
    path('modulos/categoria/add', views.crear_categoria_modulo, name='crear_categoria_modulo'),
    path('modulos/categoria/eliminar/<int:pk>/', views.eliminar_categoria_modulo, name='eliminar_categoria_modulo'),
    path('modulos/categoria/editar/<int:pk>/', views.editar_categoria_modulo, name='editar_categoria_modulo'),


]
