from django.db import models
import random

class QuestionSet(models.Model):
    choices = (
        ('Option A', 'A'),
        ('Option B', 'B'),
        ('Option C', 'C'),
        ('Option D', 'D'),
    )
    question = models.CharField(max_length=200)
    optiona = models.CharField(max_length=200)
    optionb = models.CharField(max_length=200)
    optionc = models.CharField(max_length=200)
    optiond = models.CharField(max_length=200)
    answer = models.CharField(max_length=10, choices=choices)

    def __str__(self):
        return self.question
    
class QuizSession(models.Model):
    correct = models.IntegerField(default=0)
    incorrect = models.IntegerField(default=0)
    quetions = models.ManyToManyField(QuestionSet)
    active = models.BooleanField(default=True)
    answered_questions = models.ManyToManyField(QuestionSet, related_name='answered_questions', blank=True)

    def start_session(self):
        questions = random.sample(list(QuestionSet.objects.all()), 5)
        if len(questions)<5:
            raise ValueError('Not enough questions')
        self.quetions.set(questions)
        self.save()

    def end_session(self):
        self.active = False
        self.save()




