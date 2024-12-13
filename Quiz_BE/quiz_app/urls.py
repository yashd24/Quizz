from django.urls import path
from .views import StartSession, Questions, SubmitAnswer, GetResult

urlpatterns = [
    path('start/',StartSession.as_view(), name='start_session'),
    path('quiz/<int:session_id>/question/', Questions.as_view(), name='get_question'),
    path('quiz/<int:session_id>/question/<int:question_id>/submit/', SubmitAnswer.as_view(),name = 'submit'),
    path('quiz/<int:session_id>/result/', GetResult.as_view(), name='get_result')
]
