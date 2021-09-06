from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceder, name='lagin')
]