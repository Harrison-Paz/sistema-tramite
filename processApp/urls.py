from django.urls import path
from . import views

urlpatterns = [
    path('tramites-doc/', views.docs, name='docs_index')
]