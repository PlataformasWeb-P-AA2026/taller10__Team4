from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ordenamiento.models import *

# importar los formularios de forms.py
from ordenamiento.forms import *

# Create your views here.

def index(request):
    """
        Listar los registros del modelo Parroquia y BarrioCiudadela,
        obtenidos de la base de datos.
    """
    parroquias = Parroquia.objects.all()
    barrios = BarrioCiudadela.objects.all()

    informacion_template = {
        'parroquias': parroquias,
        'numero_parroquias': len(parroquias),
        'barrios': barrios,
        'numero_barrios': len(barrios)
    }

    return render(request, 'index.html', informacion_template)


def listar_parroquias(request):
    """
        Listar los registros del modelo Parroquia.
    """
    parroquias = Parroquia.objects.all()

    informacion_template = {
        'parroquias': parroquias,
        'numero_parroquias': len(parroquias)
    }

    return render(request, 'listarParroquias.html', informacion_template)


def listar_barrios(request):
    """
        Listar los registros del modelo BarrioCiudadela.
    """
    barrios = BarrioCiudadela.objects.all()

    informacion_template = {
        'barrios': barrios,
        'numero_barrios': len(barrios)
    }

    return render(request, 'listarBarrios.html', informacion_template)


def crear_parroquia(request):
    """
        Crear un registro del modelo Parroquia.
    """
    print(request)
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()

    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario)


def editar_parroquia(request, id):
    """
        Editar un registro del modelo Parroquia.
    """
    print("---------------")
    print(request)
    print("---------------")

    parroquia = Parroquia.objects.get(pk=id)

    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)

    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario)


def crear_barrio(request):
    """
        Crear un registro del modelo BarrioCiudadela.
    """
    print(request)
    if request.method == 'POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()

    diccionario = {'formulario': formulario}

    return render(request, 'crearBarrio.html', diccionario)


def editar_barrio(request, id):
    """
        Editar un registro del modelo BarrioCiudadela.
    """
    print("---------------")
    print(request)
    print("---------------")

    barrio = BarrioCiudadela.objects.get(pk=id)

    if request.method == 'POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)

    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario)