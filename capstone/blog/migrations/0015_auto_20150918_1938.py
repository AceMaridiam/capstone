# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20150918_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tool_choice',
        ),
        migrations.AddField(
            model_name='post',
            name='tool_choice',
            field=models.CharField(default=b'Lightbox', max_length=10, choices=[(b'Lightbox', b'Lightbox'), (b'Compass', b'Compass'), (b'Pen', b'Pen')]),
        ),
    ]
