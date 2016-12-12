# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('text', models.CharField(max_length=120)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='IdealAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('my_answer_importance', models.CharField(choices=[('Very Important', 'Very Important'), ('Important', 'Important'), ('Not too important', 'Not too important')], max_length=20)),
                ('my_points', models.IntegerField(default=-1)),
                ('their_importance', models.CharField(choices=[('Very Important', 'Very Important'), ('Important', 'Important'), ('Not too important', 'Not too important')], max_length=20)),
                ('their_points', models.IntegerField(default=-1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('my_answer', models.ForeignKey(to='questionsapp.Answer', related_name='user_answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('text', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAdm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
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
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='questionsapp.Question'),
        ),
    ]
