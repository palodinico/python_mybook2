# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20150525_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 16, 30, 27, 470885), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publisher',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 16, 30, 27, 470885), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 16, 30, 27, 468885), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 16, 30, 27, 468885), auto_now=True),
            preserve_default=True,
        ),
    ]
