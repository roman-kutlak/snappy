# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templatemodel',
            name='template_content',
        ),
        migrations.AddField(
            model_name='templatemodel',
            name='content',
            field=models.TextField(default='', max_length=64000),
        ),
        migrations.AddField(
            model_name='templatemodel',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
