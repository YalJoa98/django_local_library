from django.shortcuts import render, HttpResponse
from django.views.generic import RedirectView,DetailView
from . models import Productos, Categoria
from . apps import MariabonitaConfig
import os, json, boto3

# Create your views here.
def resultados(request, *args, **kwargs):
    if request.GET["buscar"]:   
        producto = request.GET["buscar"]
        resultados = Productos.objects.filter(nombre__icontains= producto)
        return render(request, "mariabonita/resultados.html", {"resultados": resultados, "query": producto})

def index(request, *args, **kwargs):
    return render(request, "mariabonita/index.html")

def productos(request, *args, **kwargs):
    productos = Productos.objects.all()
    return render(request, "mariabonita/productos.html", {"productos": productos})
 
def categorias(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    return render(request, "mariabonita/categorias.html", {"categorias": self.categorias})

def registro(request, *args, **kwargs):
    return render(request, "mariabonita/registro.html")