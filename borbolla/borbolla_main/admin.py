from django.contrib import admin
from borbolla_main.models import Categoria , Pagina , Comentario


class PaginaAdmin(admin.ModelAdmin):
    list_display = ('titulo' , 'categoria' , 'url')

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'email' , 'fecha')


admin.site.register(Categoria)
admin.site.register(Pagina,PaginaAdmin)
admin.site.register(Comentario , ComentarioAdmin)
