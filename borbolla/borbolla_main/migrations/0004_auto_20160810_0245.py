# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-10 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borbolla_main', '0003_auto_20160810_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='categoria',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
