# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0004_auto_20150825_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='buyer',
            field=models.CharField(default=None, max_length=150, null=True, blank=True),
        ),
    ]
