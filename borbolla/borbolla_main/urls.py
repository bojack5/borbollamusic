from django.conf.urls import url
from borbolla_main import views

urlpatterns = [
    url(r'^$' , views.index , name = 'index'),
    url(r'^about/$' , views.about , name = 'about'),

]