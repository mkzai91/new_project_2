# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0003_auto_20150817_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='buyer',
            field=models.CharField(default=None, max_length=150, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='expire_date',
            field=models.DateField(default=datetime.date(2015, 9, 1)),
        ),
    ]
