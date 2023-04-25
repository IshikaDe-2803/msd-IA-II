# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import NewVideo
from .serializer import VideoSerializer
from django.http import Http404

class VideoListApiView(APIView):
    # add permission to check if user is authenticated
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the video items for given requested user
        '''
        videos = NewVideo.objects.filter(user = request.user.id)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Post a video item
        '''
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VideoDetailApiView(APIView):
    # add permission to check if user is authenticated
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def get_video(self, pk):
        try:
            return NewVideo.objects.get(pk=pk)
        except NewVideo.DoesNotExist:
            raise Http404
    
    '''
    Get a video object
    '''
    def get(self, request, pk, *args, **kwargs):
        video = self.get_video(pk=pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)

    '''
    Patch a video object
    '''
    def patch(self, request, pk, *args, **kwargs):
        video = NewVideo.objects.get(pk=pk)
        serializer = VideoSerializer(video, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    '''
    Delete a video object
    '''
    def delete(self, request, pk, *args, **kwargs):
        videos = NewVideo.objects.get(pk=pk)
        videos.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)