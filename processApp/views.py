from django.shortcuts import render
from django.db.models import Q

from mainApp import models
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def docs(request):
    return render(request, 'document/tramite.html')

@login_required(login_url="/")
def listRegister(request):
    queryset = request.GET.get("buscar")
    register = models.Register.objects.filter(public=True)
    paginator = Paginator(register, 5)
    pagina = request.GET.get("page") or 1
    categoria = paginator.get_page(pagina)
    paginaActual = int(pagina)
    paginas = range(1, categoria.paginator.num_pages + 1)
    if queryset:
        register = models.Register.objects.filter(
            Q(descripcion__icontains=queryset), public=True
        ).distinct()
    context = {
        'register': register,
        'estudiante': request.user.username,
        'pagina': pagina,
        'paginas': paginas,
        'paginaActual': paginaActual,
    }
    return render(request, "register/listar.html", context)


@login_required(login_url="/")
def listDocument(request):
    queryset = request.GET.get("buscar")
    document = models.Document.objects.filter(public=True)
    paginator = Paginator(document, 5)
    pagina = request.GET.get("page") or 1
    document = paginator.get_page(pagina)
    paginaActual = int(pagina)
    paginas = range(1, document.paginator.num_pages + 1)
    if queryset:
        register = models.Document.objects.filter(
            Q(descripcion__icontains=queryset), public=True
        ).distinct()
    context = {
        'document': document,
        'estudiante': request.user.username,
        'pagina': pagina,
        'paginas': paginas,
        'paginaActual': paginaActual,
    }
    return render(request, "document/tramite.html", context)

