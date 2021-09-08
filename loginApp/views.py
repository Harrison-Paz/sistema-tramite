from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def acceder(request):
    if request.method == "POST":
        nombre_usuario = request.POST.get("username")
        password = request.POST.get("password")
        usuario = authenticate(username=nombre_usuario, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect("home")
        else:
            messages.error(request, "Los datos son incorrectos")
    return render(request, "login/login.html")



def salir(request):
    logout(request)
    messages.info(request, "Saliste exitosamente")
    return redirect("login")





