# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20150521_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='last_name',
            new_name='family_name',
        ),
    ]
