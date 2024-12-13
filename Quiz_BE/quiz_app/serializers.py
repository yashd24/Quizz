from rest_framework import serializers
from .models import QuestionSet, QuizSession

class QuestionSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionSet
        fields = '__all__'

class QuizSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizSession
        fields = '__all__'


