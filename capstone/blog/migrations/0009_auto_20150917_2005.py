# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_tools'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tools',
            old_name='tools',
            new_name='tool',
        ),
    ]
