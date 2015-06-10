# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='著者')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='book',
            old_name='pubisher',
            new_name='publisher',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=None, verbose_name='著者', blank=True, to='cms.Author', related_name='authors'),
            preserve_default=True,
        ),
    ]
