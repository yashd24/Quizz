from .models import QuestionSet, QuizSession
from rest_framework.views import APIView
from .serializers import QuestionSetSerializer, QuizSessionSerializer
from rest_framework.response import Response
from rest_framework import status


class StartSession(APIView):
    def post(self, request):
        session = QuizSession.objects.create()
        session.start_session()
        serializer = QuizSessionSerializer(session)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Questions(APIView):
    def get(self, request, session_id):
        try:
            session = QuizSession.objects.get(id=session_id, active=True)
        except QuizSession.DoesNotExist:
            return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)

        questions = session.quetions.all().first()
        if questions:
            serializer = QuestionSetSerializer(questions)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No more questions'}, status=status.HTTP_200_OK)

class SubmitAnswer(APIView):
    def post(self, request, session_id, question_id):
        try:
            session = QuizSession.objects.get(id=session_id, active=True)
        except QuizSession.DoesNotExist:
            return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            question = QuestionSet.objects.get(id=question_id)
        except QuestionSet.DoesNotExist:
            return Response({'error': 'Question not found'}, status=status.HTTP_404_NOT_FOUND)

        choosen_option = request.data.get('choosen_option')
        is_correct = choosen_option == question.answer

        if session.answered_questions.filter(id=question_id).exists():
            return Response({'message': 'Question already answered'}, status=status.HTTP_400_BAD_REQUEST)

        if is_correct:
            session.correct += 1
        else:
            session.incorrect += 1

        session.quetions.remove(question)
        session.answered_questions.add(question)
        session.save()
        return Response({'message': 'Answer submitted'}, status=status.HTTP_200_OK)


class GetResult(APIView):
    def get(self, request, session_id):
        try:
            session = QuizSession.objects.get(id=session_id)
        except QuizSession.DoesNotExist:
            return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuizSessionSerializer(session)
        session.end_session()
        return Response(serializer.data, status=status.HTTP_200_OK)
