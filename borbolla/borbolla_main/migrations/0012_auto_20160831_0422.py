# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-31 04:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borbolla_main', '0011_auto_20160830_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2016, 8, 31, 4, 22, 45, 848487), null=True),
        ),
    ]
