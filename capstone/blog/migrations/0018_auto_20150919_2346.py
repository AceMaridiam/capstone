# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20150918_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='duration',
            field=models.CharField(max_length=255),
        ),
    ]
