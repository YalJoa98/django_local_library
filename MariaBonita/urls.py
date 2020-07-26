from django.urls import path
from . import views

app_name = 'mariabonita'

urlpatterns = [
    path('', views.index, name="index"),
    path('productos/', views.productos, name="productos"),
    path('categorias/', views.categorias, name="categorias"),
]
