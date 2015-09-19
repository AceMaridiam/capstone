# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_tool_tool_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='tool',
        ),
        migrations.AddField(
            model_name='post',
            name='tool_choice',
            field=models.ManyToManyField(to='blog.Tool'),
        ),
    ]
