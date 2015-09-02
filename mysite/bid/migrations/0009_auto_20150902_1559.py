# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0008_member_cart_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Product_ID', models.IntegerField()),
                ('text', tinymce.models.HTMLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='product',
            name='expire_date',
            field=models.DateField(default=datetime.date(2015, 9, 9)),
        ),
    ]
