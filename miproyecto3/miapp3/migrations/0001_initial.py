# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('precio', models.FloatField()),
                ('tipo', models.CharField(choices=[('N', 'Nuevo'), ('U', 'Usado')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('nombre_articulo', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
            ],
        ),
    ]
