# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20150918_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tool_choice',
            field=models.ManyToManyField(related_name='tool', to='blog.Tool'),
        ),
    ]
