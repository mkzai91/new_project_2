# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0005_auto_20150825_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bid_price',
            field=models.DecimalField(default=0, verbose_name=b'price', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='expire_date',
            field=models.DateField(default=datetime.date(2015, 9, 8)),
        ),
    ]
