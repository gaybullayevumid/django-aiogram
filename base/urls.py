from django.urls import path
from .views import BotUserAPIView, FeedbackAPIView

urlpatterns = [
    path('bot-users/', BotUserAPIView.as_view(), name='bot-users'),
    path('feedbacks/', FeedbackAPIView.as_view(), name='feedbacks'),
]
