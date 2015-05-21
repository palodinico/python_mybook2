# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20150521_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=255, default=None, verbose_name='著者名'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=255, default=None, verbose_name='著者性'),
            preserve_default=True,
        ),
    ]
