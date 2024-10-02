from .models import BotUser, Feedback
from rest_framework.serializers import ModelSerializer

class BotUserSerializers(ModelSerializer):
    class Meta:
        model = BotUser
        fields = ("name", "username", "user_id", "crated_at")


class FeedbackSerialer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("user_id", "created_at", "body")