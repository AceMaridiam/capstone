# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20150918_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mult_tool_choice',
            field=models.ManyToManyField(related_name='tool', to='blog.Tool'),
        ),
    ]
