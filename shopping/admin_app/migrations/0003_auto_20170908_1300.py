# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_auto_20170908_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessories',
            name='accessoriesbrand',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AddField(
            model_name='bottoms',
            name='bottombrand',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AddField(
            model_name='footwears',
            name='footwearbrand',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AddField(
            model_name='outerwears',
            name='outerwearbrand',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AddField(
            model_name='tops',
            name='topbrand',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]