# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0002_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='user',
            new_name='username',
        ),
    ]
