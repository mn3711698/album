# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=255)),
                ('hotelname', models.CharField(max_length=255)),
                ('accounts', models.CharField(max_length=255)),
                ('mintor_data', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('timestamp', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]
