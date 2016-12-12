from django.contrib import admin
from .models import Question, Answer, UserAnswer


# Register your models here.


# here I am tabulating answers in line for each questions
# Got ideas from tutorials and doc
# https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.TabularInline
class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdm(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]

    class Meta:
        model = Question


# admin.site.register(Question, QuestionAdm)
admin.site.register(Answer)
admin.site.register(UserAnswer)
