# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp3', '0004_auto_20151123_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='foto',
            field=models.ImageField(null=True, upload_to='miapp3/static/fotos'),
        ),
    ]
