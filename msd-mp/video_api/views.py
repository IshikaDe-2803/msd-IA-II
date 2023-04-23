# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import NewVideo
from .serializer import VideoSerializer

class VideoListApiView(APIView):
    # add permission to check if user is authenticated
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        videos = NewVideo.objects.filter(user = request.user.id)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        '''
        data = {
            "user": request.user.id,
            "title": request.data.get('title'),
            "description": request.data.get('description'), 
            "thumbnail": request.FILES.get('thumbnail'),
            "video": request.FILES.get('video'),
        }
        serializer = VideoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        video = NewVideo.objects.filter(user=request.user.id, title=request.data.get('title'))
        data = {
            "visits": request.data.get('visits'),
            "likes": request.data.get('likes'),
            "dislikes": request.data.get('dislikes'),
            "user": request.user.id,
            "title": request.data.get('title'),
            "description": request.data.get('description'), 
            "thumbnail": request.FILES.get('thumbnail'),
            "video": request.FILES.get('video'),
        }
        serializer = VideoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        videos = NewVideo.objects.filter(user=request.user.id, title=request.data.get('title'))
        videos.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)