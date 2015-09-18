# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150917_1922'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tools',
        ),
        migrations.AddField(
            model_name='post',
            name='art_tools',
            field=models.CharField(default=b'LB', max_length=2, choices=[(b'LB', b'Lightbox'), (b'Compass', b'Compass'), (b'Airbrush', b'Airbrush')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='duration',
            field=models.TimeField(),
        ),
    ]
