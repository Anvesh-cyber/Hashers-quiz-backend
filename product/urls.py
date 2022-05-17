from django.urls import path

from .views import UserView,  QuizView, QuestionView, AnswerView, ResultView

urlpatterns = [
    path("api/users/", UserView.as_view()),
    path("api/quiz/", QuizView.as_view()),
    path("api/question/", QuestionView.as_view()),
    path("api/answer/", AnswerView.as_view()),
    path("api/result/", ResultView.as_view()),

]

