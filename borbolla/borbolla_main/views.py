from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'texto1': "Crunchy, creamy, cookie, candy, cupcake!",
                    'titulo': "Index"}

    return render(request , 'borbolla_main/index.html' , context = context_dict)

def about(request):
    return HttpResponse('<h1>Pagina de About!!!</h1><br><a href="/main/">Index</a>')    
