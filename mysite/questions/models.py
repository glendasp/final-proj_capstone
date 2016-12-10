from django.db import models

# Create your models here.

# Model for the questions
class Question(models.Model):
    question = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
