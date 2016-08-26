from django.conf.urls import url
from borbolla_main import views

urlpatterns = [
    url(r'^$' , views.index , name = 'index'),
    url(r'^about/$' , views.about , name = 'about'),
    url(r'^add_category/$' , views.add_category , name = 'add_category'),
    url(r'^procesa_comentario/$' , views.procesa_comentario , name = 'procesa_comentario')
    #url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        #views.show_category, name='show_category'),

]