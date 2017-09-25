# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='RegistrationForm',
        ),
        migrations.DeleteModel(
            name='Validate',
        ),
    ]
