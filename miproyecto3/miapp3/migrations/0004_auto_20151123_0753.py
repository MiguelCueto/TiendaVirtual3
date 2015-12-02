# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp3', '0003_auto_20151112_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='nombre_articulo',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='precio',
        ),
        migrations.AddField(
            model_name='articulo',
            name='nombre_proveedor',
            field=models.ManyToManyField(to='miapp3.Proveedor'),
        ),
    ]
