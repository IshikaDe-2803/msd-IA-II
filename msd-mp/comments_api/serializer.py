from rest_framework import serializers
from video_api.models import NewVideo

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    
    class Meta:
        model = NewVideo
        fields = ["user", "username", "comment_text", "video"]