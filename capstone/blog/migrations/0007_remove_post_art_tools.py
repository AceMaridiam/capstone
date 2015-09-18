# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150917_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='art_tools',
        ),
    ]
