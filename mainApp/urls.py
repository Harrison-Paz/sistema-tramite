from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('tramite/', views.tramite, name='tramites'),
]