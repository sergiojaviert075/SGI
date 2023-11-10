import datetime
from datetime import datetime
from validadores import validador
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from administrativo.models import Persona, PersonaPerfil, Incidencia
from administrativo.forms import IncidenciaForm
from authenticaction.models import CustomUser


@login_required
@validador
def listar_misincidencias(request,search=None):
    try:
        parametros = ''
        incidencias = Incidencia.objects.filter(status=True, responsable=request.user.persona)
        if 'search' in request.GET:
            search_ = search = request.GET['search']
            parametros += '&search=' + search_
            search_ = search_.strip()
            ss = search_.split(' ')
            incidencias = incidencias.filter(Q(titulo__icontains=search) |
                                       Q(descripcion__icontains=search))

        paginator = Paginator(incidencias, 25)
        page = request.GET.get('page')
        try:
            page_object = paginator.page(page)
        except PageNotAnInteger:
            page_object = paginator.page(1)
        except EmptyPage:
            page_object = paginator.page(paginator.num_pages)

        context = {
            'page_object': page_object,
            'page_titulo': "Mis incidencias",
            'titulo': "Mis incidencias",
            'search': search,
            'parametros': parametros,
        }
        return render(request, 'misincidencias/inicio.html', context)
    except Exception as e:
        HttpResponseRedirect(f"/?info={e.__str__()}")


@login_required
def crear_miincidencia(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                form = IncidenciaForm(request.POST, request.FILES)
                instance = Incidencia(
                    responsable=request.user.persona,
                    titulo=request.POST['titulo'],
                    descripcion=request.POST['descripcion'],
                    categoria=request.POST['categoria']
                )
                instance.save(request)
                if 'archivo' in request.FILES:
                    archivo = request.FILES['archivo']
                    extension = archivo._name[archivo._name.rfind("."):]
                    archivo._name = "archincidencia_" + str(instance.id) + '_' + str(datetime.now()) + extension.lower()
                    instance.archivo = archivo
                    instance.save(request)
                return JsonResponse({"success": True, "message": 'Acción realizada con éxito!', "url": '/administrativo/misincidencias/'})
        except Exception as e:
            transaction.set_rollback(True)
            return JsonResponse({'success': False})
    else:
        form = IncidenciaForm()
    context = {
        'form': form,
        'titulo': "Adicionar incidencia",
        'page_titulo': "Adicionar incidencia",
        'height': True,
        'action': '/misincidencias/add',
        'cancelar': 'administrativo:listar_misincidencias',
    }
    return render(request, 'misincidencias/add.html', context)

@login_required
def editar_miincidencia(request, pk):
    instance = get_object_or_404(Incidencia, pk=pk)
    if request.method == 'POST':
        try:
            with transaction.atomic():
                form = IncidenciaForm(request.POST, request.FILES)
                instance.titulo = request.POST['titulo']
                instance.descripcion = request.POST['descripcion']
                instance.categoria = request.POST['categoria']
                instance.save(request)
                if 'archivo' in request.FILES:
                    archivo = request.FILES['archivo']
                    extension = archivo._name[archivo._name.rfind("."):]
                    archivo._name = "archincidencia_" + str(instance.id) + '_' + str(datetime.now()).replace('-', '_') + extension.lower()
                    instance.archivo = archivo
                    instance.save(request)
                return JsonResponse({'success': True, 'message': 'Acción realizada con éxito!', "url": '/administrativo/misincidencias/'})
        except Exception as e:
            transaction.set_rollback(True)
            return JsonResponse({'success': False})
    else:
        form = IncidenciaForm(initial={
            'titulo': instance.titulo,
            'descripcion': instance.descripcion,
            'categoria': instance.categoria,
            'archivo': instance.archivo
        })
    context = {
        'form': form,
        'titulo': "Editar incidencia",
        'page_titulo': "Editar incidencia",
        'height': True,
        'action': '/misincidencias/edit/' + str(pk),
        'cancelar': 'administrativo:listar_misincidencias',
    }
    return render(request, 'misincidencias/edit.html', context)

@login_required
def eliminar_miincidencia(request):
    try:
        instance = get_object_or_404(Incidencia, pk=int(request.POST['id']))
        if request.method == 'POST':
            instance.eliminar_registro(request)
            return JsonResponse({'success': True, 'message': 'Registro eliminado con éxito'})
    except Incidencia.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'El registro no existe'})

