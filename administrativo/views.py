from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from administrativo.models import PersonaPerfil, Persona, Incidencia
from system.models import Modulo
from django.http import JsonResponse, HttpResponseRedirect

# Create your views here.

@login_required
def consultaAdministrativos(request):
    try:
        perfiles = PersonaPerfil.objects.filter(status=True)
        total = perfiles.filter(is_administrador=True).count()
        return JsonResponse({'success': True, 'total': total})
    except PersonaPerfil.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'El registro no existe'})

@login_required
def consultaPersonas(request):
    try:
        totalpersonas = Persona.objects.filter(status=True).count()
        return JsonResponse({'success': True, 'total': totalpersonas})
    except PersonaPerfil.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'El registro no existe'})

@login_required
def consultaIncidencias(request):
    try:
        incidencias = Incidencia.objects.filter(status=True)
        total = incidencias.count()
        return JsonResponse({'success': True, 'total': total})
    except PersonaPerfil.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'El registro no existe'})


@login_required
def consultaModulos(request):
    try:
        modulos = Modulo.objects.filter(status=True, visible=True)
        total = modulos.count()
        return JsonResponse({'success': True, 'total': total})
    except PersonaPerfil.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'El registro no existe'})