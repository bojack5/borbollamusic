from django.db import models
from django.contrib import admin


class Categoria(models.Model):
    """docstring for Categoria"""
    nombre = models.CharField(max_length = 128 , unique = True ,)
    views  = models.IntegerField(default = 0)
    likes  = models.IntegerField(default = 0)
    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):

        return self.nombre	

class Pagina(models.Model):
    """docstring for Pagina"""
    titulo    = models.CharField(max_length = 128)
    categoria = models.ForeignKey(Categoria)
    
    url       = models.URLField()
    views     = models.IntegerField(default = 0)

    

    def __str__(self):

        return self.titulo	


            

            		        
		
# Create your models here.
