# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-13 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0004_auto_20170913_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='flag',
            field=models.ImageField(default='', upload_to='points/uploads/country flags'),
        ),
    ]