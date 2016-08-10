from django.contrib import admin
from borbolla_main.models import Categoria , Pagina


class PaginaAdmin(admin.ModelAdmin):
    list_display = ('titulo' , 'categoria' , 'url')


admin.site.register(Categoria)
admin.site.register(Pagina,PaginaAdmin)

