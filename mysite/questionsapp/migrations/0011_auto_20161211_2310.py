# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionsapp', '0010_auto_20161211_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idealanswer',
            name='my_answer',
        ),
        migrations.RemoveField(
            model_name='idealanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='idealanswer',
            name='their_answer',
        ),
        migrations.RemoveField(
            model_name='idealanswer',
            name='user',
        ),
    ]
