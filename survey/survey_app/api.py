from .models import Survey, Question
from rest_framework import viewsets, permissions
from .serializer import SurveySerializer, QuestionSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]

    serializer_class = SurveySerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]

    serializer_class = QuestionSerializer