from django.conf.urls import url
from borbolla_main import views

urlpatterns = [
    url(r'^$' , views.index , name = 'index'),
    url(r'^about/$' , views.about , name = 'about'),
    url(r'^add_category/$' , views.add_category , name = 'add_category'),
    url(r'^procesa_comentario/$' , views.procesa_comentario , name = 'procesa_comentario'),
    url(r'^registro/$', views.registro , name = 'registro'),
    url(r'^ingresar/$', views.login_view , name = 'ingreso'),
    url(r'^salir/$', views.logout_view , name = 'logout'),
    url(r'^academia/$', views.academia_view , name = 'academia'),
    url(r'^instalacion/$', views.instalacion_view , name = 'instalacion'),
    url(r'^instrumentos/$', views.instrumentos_view , name = 'instrumentos'),
    url(r'^audio/$', views.audio_view , name = 'audio'),
    #url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        #views.show_category, name='show_category'),

]