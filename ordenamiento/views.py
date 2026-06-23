from django.shortcuts import render, redirect

from ordenamiento.models import Parroquia, BarrioCiudadela
from ordenamiento.forms import ParroquiaForm, BarrioCiudadelaForm


def index(request):
    parroquias = Parroquia.objects.all()
    barrios = BarrioCiudadela.objects.all()

    informacion_template = {
        'parroquias': parroquias,
        'numero_parroquias': len(parroquias),
        'barrios': barrios,
        'numero_barrios': len(barrios),
    }

    return render(request, 'index.html', informacion_template)


def listar_parroquias(request):
    parroquias = Parroquia.objects.all()

    informacion_template = {
        'parroquias': parroquias,
        'numero_parroquias': len(parroquias),
    }

    return render(request, 'listarParroquias.html', informacion_template)


def listar_barrios(request):
    barrios = BarrioCiudadela.objects.all()

    informacion_template = {
        'barrios': barrios,
        'numero_barrios': len(barrios),
    }

    return render(request, 'listarBarrios.html', informacion_template)


def crear_parroquia(request):
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()

    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario)


def editar_parroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)

    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)

    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario)


def crear_barrio(request):
    if request.method == 'POST':
        formulario = BarrioCiudadelaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioCiudadelaForm()

    diccionario = {'formulario': formulario}

    return render(request, 'crearBarrio.html', diccionario)


def editar_barrio(request, id):
    barrio = BarrioCiudadela.objects.get(pk=id)

    if request.method == 'POST':
        formulario = BarrioCiudadelaForm(request.POST, instance=barrio)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioCiudadelaForm(instance=barrio)

    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario)