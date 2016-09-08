#!/usr/bin/env python3

from django import forms
from django.contrib.auth.models import User
from borbolla_main.models import Pagina , Categoria , Comentario , PerfilUsuario , Academia
from datetime import datetime


class AcademiaForm(forms.ModelForm):
    CHOICES = (
    ('GE','Guitarra'),
    ('TE','Teclado'),
    ('BA','Bateria'),
    ('BJ','Bajo'),
    ('GA','Guitarra Acustica'),
        )

    CHOICES_ENTERADO = (
        ('FB','Facebook'),
        ('GO','Google'),
        ('YT','Youtube'),
        ('WW','Otro sitio Web'),
        ('RE','Me lo recomendaron'),
        ('AL','Ya fui alumno'),
        ('PA','Pase por la academia y vi anuncio'),
        ('CO','Compre un instrumento en Borbolla'),
        ('VO','Folleto o volante'),
        ('TV', 'TV o Radio'),)
    nombre = forms.CharField(max_length=100, widget = forms.TextInput(attrs = {'onfocus':"this.value = ''",
                                                               'placeholder': 'Nombre'}))
    curso  = forms.ChoiceField(widget=forms.Select , choices=CHOICES , )
    edad   = forms.IntegerField(widget = forms.TextInput(attrs = {'onfocus':"this.value = ''",
                                                               'placeholder': 'Edad'}))
    email  = forms.EmailField(max_length=50 ,  widget = forms.TextInput(attrs = {'onfocus':"this.value = ''",
                                                               'placeholder': 'Email'}))
    celular = forms.CharField(max_length=20 , widget = forms.TextInput(attrs = {'onfocus':"this.value = ''",
                                                               'placeholder': 'Celular'}))
    enterado = forms.ChoiceField(widget=forms.Select , choices=CHOICES_ENTERADO)

    varioscursos = forms.BooleanField(required = False)
    
    variosfamiliares = forms.BooleanField(required = False)


    
    class Meta:
        model = Academia
        exclude = ('fecha',)

class CategoriaFormulario(forms.ModelForm):
    nombre = forms.CharField(max_length = 128 , 
    	                     help_text = 'Porfavor introduce un nombre de categoria.')
    views  = forms.IntegerField(widget = forms.HiddenInput() , initial = 0)
    likes  = forms.IntegerField(widget = forms.HiddenInput() , initial = 0)
    slug   = forms.CharField(widget = forms.HiddenInput() , required = False )
   
    class Meta:
        model = Categoria
        fields = ('nombre',)


class PaginaFormulario(forms.ModelForm):
    title = forms.CharField(max_length = 128,
    	                    help_text = 'Introduce el titulo de la pagina')

    url   = forms.URLField(max_length = 200 ,
                           help_text  = 'Introduce URL de la pagina')
    views = forms.IntegerField(widget = forms.HiddenInput() , initial = 0)
    
    class Meta:
        model = Pagina
        exclude = ('category',)

class ComentarioFormulario(forms.ModelForm):


    nombre  = forms.CharField(max_length  = 50 ,
    	                     help_text    = 'Nombre',
    	                     widget = forms.TextInput(attrs = {'onfocus':"this.value = ''",
    	                     	                               'placeholder': 'Nombre'}))
    email   = forms.EmailField(max_length = 50 ,
    	                     help_text    = 'Email',
    	                     widget = forms.TextInput(attrs = {'onfocus':"this.value = ''" , 
    	                     	                               'placeholder': 'Email'}))
    mensaje = forms.CharField(max_length  = 20000 ,
    	                     help_text    = 'Mensaje',
    	                     widget = forms.Textarea(attrs = {'onfocus':"this.value = ''" ,
    	                     	                               'placeholder': 'mensaje'}))	                         
    #fecha   = forms.DateField(widget = forms.HiddenInput() ,)
    
    #def save(self , *args , **kwargs):
    #    self.fecha = timezone.now()

    #    return super(ComentarioFormulario , self).save(*args , **kwargs)


    class Meta:
        model = Comentario
        exclude = ('fecha',)

class UserForm(forms.ModelForm):
    nombre   = forms.CharField(max_length = 50 , 
    	                       widget = forms.TextInput(attrs = {'onfocus':"this.value = ''",
    	                     	                                 'placeholder': 'Nombre'}))
    apellido = forms.CharField(max_length = 50 ,
    	                       widget = forms.TextInput(attrs = {'onfocus':"this.value = ''",
    	                     	                               'placeholder': 'Apellido'}))
    email    = forms.EmailField(max_length = 100 , 
    	                        widget = forms.TextInput(attrs = {'onfocus':"this.value = ''",
    	                     	                               'placeholder': 'Email'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'onfocus':"this.value = ''",
    	                     	                               'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('nombre' , 'apellido' , 'email' , 'password')

    
class LoginForm(forms.Form):
    """docstring for ContactoForm"""
    usuario = forms.CharField(max_length = 10)
    password = forms.CharField(max_length = 15 , widget=forms.PasswordInput())    







