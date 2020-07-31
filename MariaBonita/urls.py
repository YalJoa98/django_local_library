from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'mariabonita'

urlpatterns = [
    path('index/', views.Index.as_view(), name="index"),
    path('productos/', views.Producto.as_view(), name="productos"),
    path('categorias/', views.Categorias.as_view(), name="categorias"),
    path('resultados/',views.Busqueda.as_view(), name="buscar"),
    path('registro/', views.Registro.as_view(), name="registro"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)