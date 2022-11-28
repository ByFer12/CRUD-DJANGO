from django.urls import path
from . import views


urlpatterns = [
       path('create/', views.create_autor, name='crear_autor'),
       path('autores/', views.autores, name='autores'),
       path('autores/editar/<int:id>', views.editar, name='editar'),
       path('autores/eliminar/<int:id>', views.eliminar, name='eliminar'),
]
