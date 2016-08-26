from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify

from datetime import datetime


class Categoria(models.Model):
    """docstring for Categoria"""
    nombre = models.CharField(max_length = 128 , unique = True ,)
    views  = models.IntegerField(default = 0)
    likes  = models.IntegerField(default = 0)
    slug   = models.SlugField()

    def save(self , *args , **kwargs):
        self.slug = slugify(self.nombre)
        super(Categoria , self).save(*args,**kwargs)
    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):

        return self.nombre	

class Pagina(models.Model):
    """docstring for Pagina"""
    categoria = models.ForeignKey(Categoria)
    titulo    = models.CharField(max_length = 128)
    
    
    url       = models.URLField()
    views     = models.IntegerField(default = 0)

    

    def __str__(self):

        return self.titulo	


class Comentario(models.Model):
    nombre  = models.CharField(max_length =  50)
    email   = models.EmailField(max_length = 50)
    mensaje = models.TextField()
    fecha   = models.DateField(null = True , default = datetime.now)    

    def __str__(self):
        return self.nombre


            		        
		
# Create your models here.
