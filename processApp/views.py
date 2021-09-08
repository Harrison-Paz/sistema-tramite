from django.shortcuts import render
from django.db.models import Q

from mainApp import models
# from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator




# @login_required(login_url="/")
def listRegister(request):
    queryset = request.GET.get("buscar")
    register = models.Register.objects.filter(public=True)
    numerations = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']
    paginator = Paginator(register, 6)
    pagina = request.GET.get("page") or 1
    register = paginator.get_page(pagina)
    paginaActual = int(pagina)
    paginas = range(1, register.paginator.num_pages + 1)
    if queryset:
        register = models.Register.objects.filter(
            Q(descripcion__icontains=queryset), public=True
        ).distinct()
    context = {
        'registers': register,
        'estudiante': request.user.username,
        'pagina': pagina,
        'paginas': paginas,
        'paginaActual': paginaActual,
        'numerations': numerations,
    }
    return render(request, "register/listarRegister.html", context)


# @login_required(login_url="/")
def listDocument(request, id):
    queryset = request.GET.get("buscar")
    document = models.Document.objects.filter(register_id=id, public=True)
    registra = models.Register.objects.get(id=id)
    paginator = Paginator(document, 6)
    pagina = request.GET.get("page") or 1
    document = paginator.get_page(pagina)
    paginaActual = int(pagina)
    paginas = range(1, document.paginator.num_pages + 1)
    if queryset:
        document = models.Document.objects.filter(
            Q(descripcion__icontains=queryset), public=True
        ).distinct()
    context = {
        'documents': document,
        'registra': registra,
        'estudiante': request.user.username,
        'pagina': pagina,
        'paginas': paginas,
        'paginaActual': paginaActual,
    }
    return render(request, "register/listarDocument.html", context)

def tramite(request, id):
    document = models.Document.objects.get(id=id)
    requiriment = models.Type_requirement.objects.filter(document_id= id)
    context = {
        'document': document,
        'requiriments': requiriment,
    }
    return render(request, "register/tramite.html", context)


