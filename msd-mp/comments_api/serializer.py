from rest_framework import serializers
from video_api.models import NewVideo
from .models import comments

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    
    class Meta:
        model = comments
        fields = ["user", "username", "comment_text", "video"]