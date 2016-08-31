from django.contrib import admin
from borbolla_main.models import Categoria , Pagina , Comentario , Promocion , ImagenesEstaticas


class PaginaAdmin(admin.ModelAdmin):
    list_display = ('titulo' , 'categoria' , 'url')

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'email' , 'fecha')

class PromocionAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'fecha' , 'views')

class ImagenesEstaticasAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'fecha')

admin.site.register(Categoria)
admin.site.register(Pagina,PaginaAdmin)
admin.site.register(Comentario , ComentarioAdmin)
admin.site.register(Promocion , PromocionAdmin)
admin.site.register(ImagenesEstaticas , ImagenesEstaticasAdmin)
