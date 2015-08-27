# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(default=b'', max_length=150)),
                ('password', models.CharField(default=b'', max_length=15)),
                ('name', models.CharField(default=b'', max_length=150)),
                ('email', models.CharField(default=b'', max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
