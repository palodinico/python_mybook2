# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20150525_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='impression',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 16, 53, 13, 886039), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='impression',
            name='update',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 5, 25, 16, 53, 13, 886039)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 16, 53, 13, 881039), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='update',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 5, 25, 16, 53, 13, 881039)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 16, 53, 13, 883039), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='update',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 5, 25, 16, 53, 13, 883039)),
            preserve_default=True,
        ),
    ]
