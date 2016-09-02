# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-31 05:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borbolla_main', '0013_auto_20160831_0430'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenesEstaticas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('img_header', models.ImageField(default='imagenes_pagina_superior/None/no-img.jpg', upload_to='static/imagenes_pagina_superior/')),
                ('subtitulo1', models.CharField(max_length=50)),
                ('texto1', models.CharField(max_length=200)),
                ('img_chica1', models.ImageField(default='imagenes_pagina_superior/None/no-img.jpg', upload_to='static/imagenes_pagina_superior/')),
                ('subtitulo2', models.CharField(max_length=50)),
                ('texto2', models.CharField(max_length=200)),
                ('img_chica2', models.ImageField(default='imagenes_pagina_superior/None/no-img.jpg', upload_to='static/imagenes_pagina_superior/')),
                ('subtitulo_banner', models.CharField(max_length=50)),
                ('img_banner', models.ImageField(default='imagenes_pagina_superior/None/no-img.jpg', upload_to='static/imagenes_pagina_superior/')),
                ('fecha', models.DateTimeField(default=datetime.datetime.now, null=True)),
            ],
        ),
    ]