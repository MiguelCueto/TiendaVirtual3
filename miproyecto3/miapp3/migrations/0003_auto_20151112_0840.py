# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp3', '0002_articulo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
