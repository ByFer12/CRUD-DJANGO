from django.shortcuts import render, redirect, get_object_or_404
from .form import AutorForm
from .models import Autor

def Home(request):
    return render(request,'index.html')


#Creando autor
def create_autor(request):
    if request.method == 'GET':
        autor= AutorForm()
        return render(request,'libros/create.html',{'form':autor})
    else:
        autor= AutorForm(request.POST)#Obtengo los datos ingresados y lo guardo en la variable formu
        if autor.is_valid():
            autor.save()
            return redirect('autores')

def autores(request):
    autores=Autor.objects.all()
    return render(request,'libros/autores.html',{'form':autores})    



def editar(request, id):
    if request.method=="GET":
        autor=get_object_or_404(Autor,pk=id)
        form=AutorForm(instance=autor)
        return render(request,'libros/editar.html',{'form':form})
    
    else:
        autor=get_object_or_404(Autor,pk=id)
        form=AutorForm(request.POST, instance=autor)
        form.save()
        return redirect('autores')
        

def eliminar(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.delete()
    return redirect('autores')
    

# Create your views here.
