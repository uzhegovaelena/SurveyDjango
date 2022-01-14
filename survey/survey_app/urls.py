from rest_framework import routers
from .api import SurveyViewSet, QuestionViewSet

router = routers.DefaultRouter()
router.register('api/survey', SurveyViewSet, 'survey')
router.register('api/question', QuestionViewSet, 'survey')

urlpatterns = router.urls