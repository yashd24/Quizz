from django.db import models
import random

class QuestionSet(models.Model):
    question = models.CharField(max_length=200)
    optiona = models.CharField(max_length=200)
    optionb = models.CharField(max_length=200)
    optionc = models.CharField(max_length=200)
    optiond = models.CharField(max_length=200)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question
    
class QuizSession(models.Model):
    correct = models.IntegerField(default=0)
    incorrect = models.IntegerField(default=0)
    quetions = models.ManyToManyField(QuestionSet)
    active = models.BooleanField(default=True)
    user_answer = models.JSONField(default=dict)
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

    def get_result(self):
        incorrect_questions = []
        for ques in self.answered_questions.all():
            user_answer = self.user_answer[str(ques.id)]
            is_correct = user_answer == ques.answer

            if not is_correct:
                incorrect_questions.append({
                    'question': ques.question,
                    'correct_answer': ques.answer,
                    'user_answer': user_answer
                })
        
        
        return {
            'score': 5 - self.incorrect,
            'incorrect_questions': incorrect_questions
        }




