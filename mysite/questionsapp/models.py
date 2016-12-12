from django.db import models
from django.conf import settings
from django.db.models import Q
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


# Create your models here.

class QuestionAdm(models.Model):
    def get_unanswered(self, user):
        q1 = Q(useranswer__user=user)
        qs = self.exclude(q1)
        return qs


# Model for the questions app
class Question(models.Model):
    text = models.TextField()
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)

    # answers = models.ManyToManyField('Answer')

    def __unicode__(self):
        return self.text[:10]


class Answer(models.Model):
    # Making the answers related to the questions
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.text[:10]


IMPORTANCE = (('Very Important', 'Very Important'), ('Important', 'Important'),
          ('Not too important', 'Not too important'))


'''
IdealAnswer:
Gets users answer and what their want on their roommate's answer to be
This made it easier to enter few users into the database by using the /admin
'''


class IdealAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.ForeignKey(Question)
    my_answer = models.ForeignKey(Answer, related_name='user_answer')
    my_answer_importance = models.CharField(max_length=20, choices=IMPORTANCE)
    my_points = models.IntegerField(default=-1)
    their_answer = models.ForeignKey(Answer, null=True, related_name='match_answer')
    their_importance = models.CharField(max_length=20, choices=IMPORTANCE)
    their_points = models.IntegerField(default=-1)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.my_answer.text[:10]


def ans_importance(importance_level):
    if importance_level == "Very Important":
        points = 3
    elif importance_level == "Important":
        points = 2
    elif importance_level == "Not too important":
        points = 2
    else:
        points = 0
    return points
