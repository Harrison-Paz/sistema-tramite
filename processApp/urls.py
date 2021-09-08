from django.contrib import admin

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista-registro/', views.listRegister, name='lista_registro'),
    path('documentos/<int:id>', views.listDocument, name='document'),
    path('tramite-doc/<int:id>', views.tramite, name='tramite-doc')
]