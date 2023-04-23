from rest_framework import serializers
from .models import NewVideo
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewVideo
        fields = ["user", "title", "description", "visits", "likes", "dislikes", "date", "thumbnail", "video"]