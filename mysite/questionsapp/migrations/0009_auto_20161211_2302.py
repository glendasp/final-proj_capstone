# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionsapp', '0008_idealanswer_questionadm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
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
        migrations.DeleteModel(
            name='QuestionAdm',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='IdealAnswer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
