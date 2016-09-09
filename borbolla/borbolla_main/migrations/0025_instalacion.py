# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-09 02:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borbolla_main', '0024_auto_20160908_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instalacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('celular', models.CharField(max_length=20)),
                ('descripcion_del_proyecto', models.TextField()),
                ('fecha', models.DateTimeField(default=datetime.datetime.now, null=True)),
            ],
            options={
                'verbose_name_plural': 'Instalaciones',
                'verbose_name': 'Instalacion',
            },
        ),
    ]