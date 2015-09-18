# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150917_2005'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tools',
            new_name='Tool',
        ),
    ]
