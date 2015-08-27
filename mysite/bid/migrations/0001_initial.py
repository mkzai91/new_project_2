# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import filebrowser.fields
from django.conf import settings
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('expire_date', models.DateField(default=datetime.date(2015, 8, 24))),
                ('bid_price', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('photo', models.ImageField(upload_to=b'')),
                ('website', models.CharField(max_length=500)),
                ('description', tinymce.models.HTMLField()),
                ('total_view', models.IntegerField(default=0)),
                ('today_view', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkSheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=150)),
                ('file', models.ImageField(upload_to=b'')),
                ('pub_date', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('pdf', models.FileField(upload_to=b'')),
                ('image', filebrowser.fields.FileBrowseField(default=b'', max_length=200, null=True, verbose_name=b'Image', blank=True)),
                ('creator', models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
