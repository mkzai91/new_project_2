# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0007_auto_20150901_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='cart_size',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
