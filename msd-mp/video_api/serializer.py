from rest_framework import serializers
from .models import NewVideo
class VideoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = NewVideo
        fields = ["user", "username", "title", "description", "visits", "likes", "dislikes", "date", "thumbnail", "video", "id"]