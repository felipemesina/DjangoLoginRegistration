# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 03:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20170925_0327'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
