# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0006_auto_20150901_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bid_price',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
        ),
    ]
