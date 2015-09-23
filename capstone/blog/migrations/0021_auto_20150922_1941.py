# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_post_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='description',
            field=models.CharField(default=b'Tool Description', max_length=255),
        ),
        migrations.AddField(
            model_name='tool',
            name='name',
            field=models.CharField(default=b'Tool Name', max_length=255),
        ),
    ]
