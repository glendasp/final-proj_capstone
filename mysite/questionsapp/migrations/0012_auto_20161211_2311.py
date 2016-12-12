# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionsapp', '0011_auto_20161211_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='idealanswer',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='question',
            name='date_created',
        ),
    ]
