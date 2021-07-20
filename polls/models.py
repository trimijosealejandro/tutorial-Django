from django.db import models
from django.db.models.fields import CharField, DateField

class Question (models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Models):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = CharField(max_length=100)
    voice = models.IntegerField(default=0)
