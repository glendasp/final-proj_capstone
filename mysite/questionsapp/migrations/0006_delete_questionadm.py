# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionsapp', '0005_auto_20161212_0428'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionAdm',
        ),
    ]
