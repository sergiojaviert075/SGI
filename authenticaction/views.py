import datetime
from datetime import date, datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db import transaction

from authenticaction.forms import CustomUserCreationForm, CustomLoginForm
from authenticaction.models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from baseapp.models import Persona
from administrativo.models import PersonaPerfil, Genero


def register(request):
    if request.method == 'POST':
        try:
            password = request.POST['password']
            confirmar_password = request.POST['confirmar-password']
            if password != confirmar_password:
                return JsonResponse({"success": False, "errors": 'Las contraseñas no son iguales'})
            if 'cedula' not in request.POST and 'pasaporte' not in request.POST and 'ruc' not in request.POST:
                return JsonResponse({"success": False, "errors": 'Por favor, ingrese identificación'})
            if Persona.objects.filter(status=True, cedula=request.POST['cedula']):
                return JsonResponse({"success": False, "errors": 'Ya se encuentra registrada esta persona con la misma cédula'})
            if Persona.objects.filter(status=True, cedula=request.POST['pasaporte']):
                return JsonResponse({"success": False, "errors": 'Ya se encuentra registrada esta persona con el mismo pasaporte'})
            if Persona.objects.filter(status=True, cedula=request.POST['ruc']):
                return JsonResponse({"success": False, "errors": 'Ya se encuentra registrada esta persona con el mismo ruc'})
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
            password = password.replace(' ', '')
            username = request.POST['nombres'].replace(' ', '').lower()  # Eliminar espacios y líneas nuevas
            usuario = CustomUser.objects.create_user(username, password)
            usuario.save()
            instance.usuario = usuario
            instance.save(request)
            persona_perfil = PersonaPerfil(
                persona=instance,
                is_usuariofinal=True
            )
            persona_perfil.save(request)
            return JsonResponse({"success": True, "message": 'Registro completado con éxito!', "url": '/accounts/login/'})
        except Exception as ex:
            transaction.set_rollback(True)
            return JsonResponse({"success": False, "errors": 'Ha ocurrido un error'})
    else:
        contexto = {
            'generos': Genero.objects.filter(status=True),
            'page_titulo': 'Registro',
            'titulo': 'Registro'
        }
    return render(request, 'registration/register.html', contexto)


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    next_url = request.GET.get('next', '')  # Obtener la URL de redirección desde el parámetro 'next'
                    if next_url:
                        return HttpResponseRedirect(next_url)  # Redirigir a la URL especificada
                    return redirect('home')  # Redirigir al usuario a la página de inicio después del inicio de sesión
                else:
                    messages.error(request, 'Tu cuenta está desactivada. Por favor, contacta al administrador.')
            else:
                messages.error(request, 'Tu cuenta no se encuentra autenticada.')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = CustomLoginForm(request)

    context = {
        'page_titulo': 'Inicio de sesión',
        'form': form,
    }
    return render(request, 'registration/login.html',context)


def custom_logout(request):
    logout(request)
    return redirect(reverse('accounts:login'))  # Cambia 'login' a la página de inicio de sesión de tu aplicación
