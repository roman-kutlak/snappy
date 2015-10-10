# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('num_params', models.PositiveSmallIntegerField()),
                ('signature', models.CharField(blank=True, max_length=256)),
                ('template_content', models.TextField(max_length=65000)),
            ],
            options={
                'ordering': ['signature'],
            },
        ),
    ]
