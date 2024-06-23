from django.db import models

# Create your models here.

class Question(models.Model):
    question_text=models.TextField(max_length=500)
    publish_date=models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.question_text

class Choices(models.Model):
    question_text=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=100)
    votes=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text