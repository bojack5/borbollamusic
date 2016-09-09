from django.contrib import admin
from borbolla_main.models import Categoria , Pagina , Comentario , Promocion ,Testimonio , Persona , PerfilUsuario , Academia , Instalacion


class PaginaAdmin(admin.ModelAdmin):
    list_display = ('titulo' , 'categoria' , 'url')

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'email' , 'fecha')

class PromocionAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'fecha' , 'views')

class TestimonioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre' ,)

class AcademiaAdmin(admin.ModelAdmin):    
    list_display = ('nombre','curso','edad','fecha')

class InstalacionAdmin(admin.ModelAdmin):    
    list_display = ('nombre','email','celular','fecha')

admin.site.register(Categoria)
admin.site.register(Pagina,PaginaAdmin)
admin.site.register(Comentario , ComentarioAdmin)
admin.site.register(Promocion , PromocionAdmin)
admin.site.register(Testimonio , TestimonioAdmin)
admin.site.register(Persona , PersonaAdmin)
admin.site.register(PerfilUsuario)
admin.site.register(Academia , AcademiaAdmin)
admin.site.register(Instalacion , InstalacionAdmin)