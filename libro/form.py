from django import forms #importamos el paquete form para que django cree el formulario por nosotros
from .models import Autor #importamos el modelo del que django creara el form


class AutorForm(forms.ModelForm):  #creamos la clase que creara al formulario
    class Meta: # clase metadatos para datos extras
        model=Autor # variable para instanciar al modeo en cuestion
        fields=['nombre', 'apellidos', 'nacionalidad', 'descripcion'] #Listar los campos para los datos del form
