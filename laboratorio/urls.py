# laboratorio/urls.py

from django.urls import path
from . import views  # Importar las vistas desde el archivo views.py

urlpatterns = [
    path('', views.index, name='index'),  # Ruta raíz que apunta a la vista index
]
