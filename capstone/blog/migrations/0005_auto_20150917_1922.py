# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150914_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('art_tools', models.CharField(default=b'LB', max_length=2, choices=[(b'LB', b'Lightbox'), (b'Compass', b'Compass'), (b'Airbrush', b'Airbrush')])),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='duration',
            field=models.TimeField(default=datetime.datetime(2015, 9, 18, 2, 22, 37, 198547, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='comments', to='blog.Post'),
        ),
    ]
