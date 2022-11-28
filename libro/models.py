from django.db import models

class Autor(models.Model):
    id =models.AutoField(primary_key=True)          #Son las columnas de las tablas(Los atributos)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellidos = models.CharField(max_length=100, blank=False, null=False)
    nacionalidad = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    Fecha_creacion=models.DateField('Fecha de creacion', auto_now=True, auto_now_add=False)
    

    def __str__(self):
        return self.nombre
    
    class Meta: #Meta indica metadatos, datos extras que le queremos colocar a la app 
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo =models.CharField('Titulo',max_length=100, blank=False, null=False)
    fecha_publicada = models.DateField('Fecha publicada', blank=False, null=False) 
    autor = models.ManyToManyField(Autor)
    fecha_creacion=models.DateField('Fecha de creacion', auto_now=True, auto_now_add=False)
    
    
    def __str__(self):
        return self.titulo
    
    
    class Meta:
        verbose_name='Libro'
        verbose_name_plural='Libros'