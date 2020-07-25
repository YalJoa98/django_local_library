from django.shortcuts import render, HttpResponse
from . models import Productos, Categoria

# Create your views here.
def index(request):
    return render(request, "mariabonita/base.html")

def productos(request):
    productos = Productos.objects.all()
    return render(request, "mariabonita/productos.html", {"productos": productos})

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "mariabonita/categorias.html", {"categorias": categorias})

