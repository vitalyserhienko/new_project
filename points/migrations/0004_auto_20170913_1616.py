# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-13 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0003_auto_20170913_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='<django.db.models.fields.CharField><django.db.models.fields.AutoField>',
            new_name='flag',
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]