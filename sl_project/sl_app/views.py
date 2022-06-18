from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Tarjeta

def index(request):
    """Vista o función que atiende la url GET /"""
    return render(request, 'sl_app/index.html')

def acerca_de(request):
    """Vista o función que atiende la url GET /"""
    return render(request, 'sl_app/acerca-de.html')

def contacto(request):
    """Vista o función que atiende la url GET /"""
    return render(request, 'sl_app/contacto.html')

def servicios(request):
    """Vista o función que atiende la url GET /"""
    return render(request, 'sl_app/servicios.html')

def tarjetas(request):
    """Vista o función que atiende la url GET /"""
    tarjetas_all = Tarjeta.objects.all()
    return render(request, 'sl_app/tarjetas.html',
        {
            "tarjetas" : tarjetas_all
        }
    )


def login_usuario(request):
    """Vista o función que atiende la url GET /login"""
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        next = request.GET.get("next", "/")
        acceso = authenticate(username=username, password=password)
        if acceso != None:
            login(request,acceso)
            return redirect (next)
        else:
            msg = "Datos incorrectos, intente de nuevo"
    else:
        msg = ""

    return render(request, 'sl_app/login.html', {"msg": msg})
