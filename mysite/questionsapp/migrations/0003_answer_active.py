# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionsapp', '0002_auto_20161210_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
