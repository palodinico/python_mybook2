# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_auto_20150525_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 17, 0, 44, 597818), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 17, 0, 44, 597818), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 17, 0, 44, 593818), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 17, 0, 44, 593818), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='impression',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 17, 0, 44, 599819), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='impression',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 17, 0, 44, 599819), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 17, 0, 44, 595818), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 17, 0, 44, 595818), auto_now=True),
            preserve_default=True,
        ),
    ]
