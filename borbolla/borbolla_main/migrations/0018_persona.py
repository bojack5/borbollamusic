# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-01 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borbolla_main', '0017_auto_20160831_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=100)),
                ('texto', models.TextField(max_length=500)),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
            ],
        ),
    ]