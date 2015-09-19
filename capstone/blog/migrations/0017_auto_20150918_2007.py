# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_post_mult_tool_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mult_tool_choice',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tool_choice',
        ),
        migrations.AddField(
            model_name='post',
            name='tool_choice',
            field=models.ManyToManyField(related_name='tool', to='blog.Tool'),
        ),
    ]
