from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'mariabonita'

urlpatterns = [
    path('index/', views.index, name="index"),
    path('productos/', views.productos, name="productos"),
    path('categorias/', views.categorias, name="categorias"),
    path('resultados/',views.resultados, name="buscar"),
    path('registro/', views.registro, name="registro"),
]

urlpatterns += static(settings.DEFAULT_FILE_STORAGE, document_root = settings.MEDIA_ROOT)