import datetime
from datetime import datetime
from validadores import validador
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from core.utils import is_ajax
from administrativo.models import Persona, PersonaPerfil
from baseapp.forms import PersonaForm
from authenticaction.models import CustomUser


@login_required
@validador
def listar_personas(request,search=None):
    try:
        parametros = ''
        personal = Persona.objects.filter(status=True)
        if 'search' in request.GET:
            search_ = search = request.GET['search']
            parametros += '&search=' + search_
            search_ = search_.strip()
            ss = search_.split(' ')
            if len(ss) == 1:
                personal = personal.filter(Q(nombres__icontains=search) |
                                           Q(apellido1__icontains=search) |
                                           Q(apellido2__icontains=search) |
                                           Q(cedula__icontains=search) |
                                           Q(pasaporte__icontains=search))
            else:
                personal = personal.filter((Q(apellido1__icontains=ss[0]) & Q(apellido2__icontains=ss[1])) |
                                           (Q(nombres__icontains=ss[0]) & Q(nombres__icontains=ss[1])))

        paginator = Paginator(personal, 25)
        page = request.GET.get('page')
        try:
            page_object = paginator.page(page)
        except PageNotAnInteger:
            page_object = paginator.page(1)
        except EmptyPage:
            page_object = paginator.page(paginator.num_pages)

        context = {
            'page_object': page_object,
            'page_titulo': "Personas",
            'titulo': "Personas",
            'search': search,
            'parametros': parametros,
        }
        return render(request, 'personas/inicio.html', context)
    except Exception as e:
        HttpResponseRedirect(f"/?info={e.__str__()}")


@login_required
def crear_persona(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                form = PersonaForm(request.POST, request.FILES)
                filtro = Q(status = True)
                if not request.POST['cedula'] and not request.POST['pasaporte'] and not request.POST['ruc']:
                    return JsonResponse(
                        {'success': False, 'message': 'Por favor, ingrese su identificación'})
                if request.POST['cedula']:
                    filtro = filtro & Q(cedula=request.POST['cedula'])
                elif request.POST['pasaporte']:
                    filtro = filtro & Q(pasaporte=request.POST['pasaporte'])
                elif request.POST['ruc']:
                    filtro = filtro & Q(ruc=request.POST['ruc'])
                persona = Persona.objects.filter(filtro)
                if not persona.exists():
                    instance = Persona(
                        nombres=request.POST['nombres'],
                        apellido1=request.POST['apellido1'],
                        apellido2=request.POST['apellido2'],
                        cedula=request.POST['cedula'],
                        pasaporte=request.POST['pasaporte'],
                        ruc=request.POST['ruc'],
                        direccion=request.POST['direccion'],
                        genero_id=int(request.POST['genero']),
                        fecha_nacimiento=request.POST['fecha_nacimiento'],
                        correo_electronico=request.POST['correo_electronico'],
                        telefono=request.POST['telefono'],
                    )
                    instance.save(request)
                    if 'foto' in request.FILES:
                        archivo = request.FILES['foto']
                        archivo._name = "fotoperfil_" + str(instance.id) + '_' + str(datetime.now())
                        instance.foto = archivo
                        instance.save(request)
                    identificacion = '*'
                    if instance.cedula:
                        identificacion = instance.cedula
                    elif instance.pasaporte:
                        identificacion = instance.pasaporte
                    elif instance.ruc:
                        identificacion = instance.ruc
                    password = identificacion.replace(' ', '')
                    password = password.lower()
                    username = request.POST['nombres'].replace(' ','').lower()  # Eliminar espacios y líneas nuevas
                    usuario = CustomUser.objects.create_user(username, password)
                    usuario.save()
                    instance.usuario = usuario
                    instance.save(request)
                    persona_perfil = PersonaPerfil(
                        persona=instance,
                        is_usuariofinal=True
                    )
                    persona_perfil.save(request)
                    return JsonResponse({"success": True, "message": 'Acción realizada con éxito!', "url": '/administrativo/personas/'})
                return JsonResponse({'success': False, 'message': 'La persona se encuentra registrada con la misma identificación'})
        except Exception as e:
            transaction.set_rollback(True)
            return JsonResponse({'success': False})
    else:
        form = PersonaForm()
        form.no_requerir()
    context = {
        'form': form,
        'titulo': "Adicionar persona",
        'page_titulo': "Adicionar persona",
        'height': True,
        'action': '/personas/add',
        'cancelar': 'administrativo:listar_personas',
    }
    return render(request, 'personas/add.html', context)

@login_required
def editar_persona(request, pk):
    instance = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        try:
            with transaction.atomic():
                form = PersonaForm(request.POST, request.FILES)
                instance.direccion = request.POST['direccion']
                instance.genero_id = request.POST['genero']
                instance.fecha_nacimiento = request.POST['fecha_nacimiento']
                instance.correo_electronico = request.POST['correo_electronico']
                instance.telefono = request.POST['telefono']
                instance.save(request)
                if 'foto' in request.FILES:
                    archivo = request.FILES['foto']
                    extension = archivo._name[archivo._name.rfind("."):]
                    archivo._name = "fotoperfil_" + str(instance.id) + '_' + str(datetime.now()).replace('-', '_') + extension.lower()
                    instance.foto = archivo
                    instance.save(request)
                return JsonResponse({'success': True, 'message': 'Acción realizada con éxito!', "url": '/administrativo/personas/'})
        except Exception as e:
            transaction.set_rollback(True)
            return JsonResponse({'success': False})
    else:
        form = PersonaForm(initial={
            'nombres': instance.nombres,
            'apellido1': instance.apellido1,
            'apellido2': instance.apellido2,
            'cedula': instance.cedula,
            'pasaporte': instance.pasaporte,
            'ruc': instance.ruc,
            'direccion': instance.direccion,
            'genero': instance.genero,
            'fecha_nacimiento': instance.fecha_nacimiento.strftime('%Y-%m-%d'),
            'correo_electronico': instance.correo_electronico,
            'telefono': instance.telefono,
            'foto': instance.foto,
        })
    form.no_necesarios()
    context = {
        'form': form,
        'titulo': "Editar persona",
        'page_titulo': "Editar persona",
        'height': True,
        'action': '/personas/edit/' + str(pk),
        'cancelar': 'administrativo:listar_personas',
    }
    return render(request, 'personas/edit.html', context)

@login_required
def eliminar_persona(request):
    try:
        instance = get_object_or_404(Persona, pk=int(request.POST['id']))
        if request.method == 'POST':
            instance.eliminar_registro(request)
            return JsonResponse({'success': True, 'message': 'Registro eliminado con éxito'})
    except Persona.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'El registro no existe'})


@login_required
def activar_desactivar_perfil(request):
    try:
        id = int(request.POST['pk'])
        tipo = int(request.POST['tipo'])
        estado = int(request.POST['estado'])
        estado = True if estado == 1 else False
        instance = get_object_or_404(PersonaPerfil, persona_id=id)
        if request.method == 'POST':
            perfil_persona = PersonaPerfil.objects.filter(status=True, persona_id=id)
            if perfil_persona.exists():
                perfil_persona = perfil_persona.first()
                #PERFIL TIPO ADMINISTRATIVO
                if tipo == 1:
                    perfil_persona.is_administrador = estado
                    perfil_persona.save(request)
                elif tipo == 2:
                    perfil_persona.is_agente = estado
                    perfil_persona.save(request)


            return JsonResponse({'success': True, 'message': 'Acción realizada con éxito'})
    except PersonaPerfil.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'El registro no existe'})

@login_required
def resetear_clave(request):
    try:
        with transaction.atomic():
            persona = Persona.objects.get(pk=request.POST['id'])
            persona.usuario.set_password(str(persona.get_card_id()))
            persona.usuario.save()
            return JsonResponse({'success': True, 'message': 'Clave reseteada correctamente'})

    except Exception as ex:
        transaction.set_rollback(True)
        return JsonResponse({'success': False, 'message': 'Error al resetear la clave'})

