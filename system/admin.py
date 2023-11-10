from django.contrib import admin

# Register your models here.
from system.models import Pais, Provincia, Canton, Parroquia, CategoriaModulo, Modulo, AccesoModulo

admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Canton)
admin.site.register(Parroquia)
admin.site.register(CategoriaModulo)
admin.site.register(Modulo)
admin.site.register(AccesoModulo)