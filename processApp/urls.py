from django.urls import path
from . import views

urlpatterns = [
    path('lista-registro/', views.listRegister, name='lista_registro'),
    path('documentos/<int:id>', views.listDocument, name='document')
]