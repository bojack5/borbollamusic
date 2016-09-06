from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.core.urlresolvers import reverse

from borbolla_main.forms import CategoriaFormulario , ComentarioFormulario , UserForm , LoginForm
from borbolla_main.models import Categoria , Promocion , Comentario , Testimonio , Persona


from mail import Email
def index(request):
    form = ComentarioFormulario()
    lista_promociones = Promocion.objects.order_by('-id')
    
    superior = Comentario.objects.order_by('-fecha')[0]
    testimonios = Testimonio.objects.order_by('-id')[:3]
    personas = Persona.objects.order_by('-id')[:3]
    
    promo1 = lista_promociones[0]
    promo2 = lista_promociones[1]
    promo3 = lista_promociones[2]
    promo4 = lista_promociones[3]
    promo5 = lista_promociones[4]
    promo6 = lista_promociones[5]
    promo7 = lista_promociones[6]

    
    category_list = Categoria.objects.order_by('-likes')[:5]


    context_dict = {'personas': personas ,
                    'testimonios': testimonios ,
                    'promo1' : promo1,
                    'promo2' : promo2,
                    'promo3' : promo3,
                    'promo4' : promo4,
                    'promo5' : promo5,
                    'promo6' : promo6,
                    'promo7' : promo7,
                    'categorias': category_list,
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

def registro(request):
    registrado = False

    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            email    = request.POST['email']
            password = request.POST['password']

            user = User.objects.create_user(username = nombre,
                                            last_name = apellido,
                                            email     = email , 
                                            password  = password)

            #hasheo de password ocurre aqui
            user.set_password(user.password)
            user.save()

            registrado = True
        else:
            print(form.errors ,)
    else:
        form = UserForm()
        

    return render(request , 
                  'borbolla_main/registro.html' ,
                  {'user_form': form,
                  'registered': registrado})

def login_view(request):
    
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')

        user = authenticate(username = usuario , password = password)

        if user:
            if user.is_active:
                login(request , user)
                print('entro por reverse')
                return index(request)
            else:
                
                return HttpResponse('Tu cuenta ha sido desabilitada')
        else:
            print("Invalid login details: {0}, {1}".format(usuario, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        print('entro por ultimo') 
        form = LoginForm()   
        
        return render(request , 'borbolla_main/login.html',{'form' : form})

def logout_view(request):
    logout(request)             
    return HttpResponseRedirect('/main/')        