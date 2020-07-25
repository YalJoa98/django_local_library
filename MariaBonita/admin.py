from django.contrib import admin
from django.contrib.admin.templatetags.admin_urls import admin_urlquote

from .models import Productos, Categoria
# Register your models here.

admin.site.register(Productos)
admin.site.register(Categoria)