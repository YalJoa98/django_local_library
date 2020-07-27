from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'mariabonita'

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('productos/', views.Productos.as_view(), name="productos"),
    path('categorias/', views.Categorias.as_view(), name="categorias"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)