from .models import BotUser, Feedback
from .serializers import BotUserSerializers, FeedbackSerialer
from rest_framework.generics import ListCreateAPIView

# Create your views here.

class BotUserAPIView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializers


class FeedbackAPIView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerialer