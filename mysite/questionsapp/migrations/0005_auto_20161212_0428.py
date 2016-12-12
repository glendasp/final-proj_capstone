# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionsapp', '0004_auto_20161211_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdealAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('my_answer_importance', models.CharField(choices=[('Very Important', 'Very Important'), ('Important', 'Important'), ('Not too important', 'Not too important')], max_length=20)),
                ('my_points', models.IntegerField(default=-1)),
                ('their_importance', models.CharField(choices=[('Very Important', 'Very Important'), ('Important', 'Important'), ('Not too important', 'Not too important')], max_length=20)),
                ('their_points', models.IntegerField(default=-1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAdm',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='questionsapp.Question', default=datetime.datetime(2016, 12, 12, 4, 27, 56, 4704, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.TextField(default=datetime.datetime(2016, 12, 12, 4, 28, 18, 806448, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idealanswer',
            name='my_answer',
            field=models.ForeignKey(to='questionsapp.Answer', related_name='user_answer'),
        ),
        migrations.AddField(
            model_name='idealanswer',
            name='question',
            field=models.ForeignKey(to='questionsapp.Question'),
        ),
        migrations.AddField(
            model_name='idealanswer',
            name='their_answer',
            field=models.ForeignKey(to='questionsapp.Answer', related_name='match_answer', null=True),
        ),
        migrations.AddField(
            model_name='idealanswer',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
