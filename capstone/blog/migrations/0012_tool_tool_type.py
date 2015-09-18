# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_tool_tool_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='tool_type',
            field=models.CharField(default=datetime.datetime(2015, 9, 18, 4, 27, 50, 621717, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
