import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'borbolla.settings')
import django

django.setup()
from mail import Email
from borbolla_main.models import Academia , Instalacion
from datetime import datetime
mensaje = '..'
if datetime.now().day == 13:
    mensaje = '''<br><br><h1>Pedidos de clase muestra via la pagina este mes</h1>
              <ol>
              '''

    for persona in Academia.objects.all():
        if persona.fecha.month == datetime.now().month:
            mensaje += '''
                        <li> <b>Nombre :</b> %s <br>
                        <b>Curso : </b>%s <br>
                        <b>edad :</b> %s <br>
                        <b>Email :</b> %s <br>
                        <b>Celular :</b> %s <br>
                        <b>Enterado : </b>%s <br>
                        <b>VariosCursos :</b> %s <br>
                        <b>VariosFamiliares :</b> %s <br>
                        <b>fecha :</b> %s <br></li><br>'''%(persona.nombre,
                        	                   persona.curso,
                        	                   persona.edad,
                        	                   persona.email,
                        	                   persona.celular,
                        	                   persona.enterado,
                        	                   persona.varioscursos,
                        	                   persona.variosfamiliares,
                        	                   persona.fecha)
    mensaje += '</ol><br><br><h1>Pedidos de Instalaciones </h1> <ol>'

    for instalacion in Instalacion.objects.all():
        if instalacion.fecha.month == datetime.now().month:
            mensaje += '''
                        <li> <b>Nombre :</b> %s <br>                    
                        <b>Email :</b> %s <br>
                        <b>Celular :</b> %s <br>
                        <b>Descripcion del proyecto :</b> %s<br>
                        <b>Fecha : %s</b><br>
                        </li><br>'''%(instalacion.nombre,
                        	                   instalacion.email,
                        	                   instalacion.celular,
                        	                   instalacion.descripcion_del_proyecto,
                        	                   instalacion.fecha,
                        	                   )
    mensaje += '</ol><br><br>    '


    if "<li>" in mensaje:
        Email('luis@4suredesign.com','Prueba','',nombre = '', email = '', mensaje = mensaje)
    else:
        Email('luis@4suredesign.com','Personas','',nombre = , email = '' , mensaje = 'No hubo pedidos este mes')