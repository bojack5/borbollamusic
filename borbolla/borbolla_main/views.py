from django.shortcuts import render
from django.http import HttpResponse
from borbolla_main.forms import CategoriaFormulario , ComentarioFormulario
from borbolla_main.models import Categoria

from mail import Email
def index(request):
    form = ComentarioFormulario()

    category_list = Categoria.objects.order_by('-likes')[:5]

    context_dict = {'categorias': category_list,
                    'titulo': "Borbolla Music",
                    'form' : form}

    return render(request , 'borbolla_main/index.html' , context = context_dict)

def about(request):
    return HttpResponse('<h1>Pagina de About!!!</h1><br><a href="/main/">Index</a>')   

def procesa_comentario(request):
    form = ComentarioFormulario()

    if request.method == 'POST':
        form = ComentarioFormulario(request.POST)

        if form.is_valid():
            form.save(commit = True)
            nombre = request.POST.get('nombre','')
            e_mail = request.POST.get('email','')
            mensaje = request.POST.get('mensaje','')
            email = Email('luis@4suredesign.com','Nuevo mensaje de pagina web','hola como estas',nombre = nombre,email = e_mail,mensaje = mensaje)
            return index(request)
        else:
            print(form.errors)
    print("Paso por procesa...")        
    return index(request ,)        


def add_category(request):
    form = CategoriaFormulario()

    if request.method == 'POST':
        form = CategoriaFormulario(request.POST)

        if form.is_valid():
            form.save(commit = True)
            
            return index(request)
        else:
            print(form.errors)

    return render(request , 'borbolla_main/add_category.html' , {'form' : form})   

