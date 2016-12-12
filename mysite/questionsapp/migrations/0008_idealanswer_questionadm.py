# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionsapp', '0007_auto_20161211_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdealAnswer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('my_answer_importance', models.CharField(max_length=20, choices=[('Very Important', 'Very Important'), ('Important', 'Important'), ('Not too important', 'Not too important')])),
                ('my_points', models.IntegerField(default=-1)),
                ('their_importance', models.CharField(max_length=20, choices=[('Very Important', 'Very Important'), ('Important', 'Important'), ('Not too important', 'Not too important')])),
                ('their_points', models.IntegerField(default=-1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('my_answer', models.ForeignKey(related_name='user_answer', to='questionsapp.Answer')),
                ('question', models.ForeignKey(to='questionsapp.Question')),
                ('their_answer', models.ForeignKey(related_name='match_answer', null=True, to='questionsapp.Answer')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAdm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
    ]
