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
from core.core import CATEGORIAS


@login_required
@validador
def listar_incidencias(request,search=None, id_categoria=None):
    try:
        parametros = ''
        incidencias = Incidencia.objects.filter(status=True)
        if 'search' in request.GET:
            search_ = search = request.GET['search']
            parametros += '&search=' + search_
            search_ = search_.strip()
            ss = search_.split(' ')
            if len(ss) == 1:
                incidencias = incidencias.filter(Q(titulo__icontains=search) |
                                                 Q(descripcion__icontains=search) |
                                                 Q(responsable__nombres__icontains=search) |
                                                 Q(responsable__apellido1__icontains=search) |
                                                 Q(responsable__apellido2__icontains=search) |
                                                 Q(responsable__cedula__icontains=search) |
                                                 Q(responsable__pasaporte__icontains=search)
                                                 )
            else:
                incidencias = incidencias.filter(Q(titulo__icontains=search) |
                                                 Q(descripcion__icontains=search) |
                                                 (Q(responsable__apellido1__icontains=ss[0]) & Q(responsable__apellido2__icontains=ss[1])) |
                                                 (Q(responsable__nombres__icontains=ss[0]) & Q(responsable__nombres__icontains=ss[1]))
                                                 )
        if 'id_categoria' in request.GET:
            id_categoria = request.GET['id_categoria']
            if int(id_categoria) > 0:
                parametros += '&id_categoria=' + str(id_categoria)
                incidencias = incidencias.filter(categoria=int(id_categoria))

        paginator = Paginator(incidencias.order_by("categoria"), 25)
        page = request.GET.get('page')
        try:
            page_object = paginator.page(page)
        except PageNotAnInteger:
            page_object = paginator.page(1)
        except EmptyPage:
            page_object = paginator.page(paginator.num_pages)

        context = {
            'page_object': page_object,
            'page_titulo': "Incidencias registradas",
            'titulo': "Incidencias registradas",
            'search': search,
            'id_categoria': int(id_categoria),
            'parametros': parametros,
            'categorias': CATEGORIAS,
        }
        return render(request, 'gestionincidencias/inicio.html', context)
    except Exception as e:
        HttpResponseRedirect(f"/?info={e.__str__()}")
