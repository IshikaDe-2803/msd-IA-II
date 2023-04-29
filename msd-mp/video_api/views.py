from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import permissions    
from .models import NewVideo
from .serializer import VideoSerializer
from django.http import Http404
from rest_framework.parsers import MultiPartParser
from django.db.models import Q

class VideoListApiView(APIView):
    serializer_class = VideoSerializer
    parser_classes = (MultiPartParser, )

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the video items for given requested user
        '''
        videos = NewVideo.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Post a video item
        '''
        data = {
            "user": request.data.get('user'),
            "username": request.data.get('username'),
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
    
class VideoDetailApiView(APIView):
    serializer_class = VideoSerializer

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
        data = {
            "user": request.data.get("user"),
            "likes": request.data.get("likes"),
            "dislikes": request.data.get("dislikes"), 
            "visits": request.data.get("visits"), 
            "id": request.data.get("id"),             
        }
        serializer = VideoSerializer(video, data=data, partial=True)
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

class VideoTrendingApiView(APIView):
    serializer_class = VideoSerializer
    def get(self, request, *args, **kwargs):
        '''
        List all the video items for given requested user
        '''
        videos = sorted(NewVideo.objects.all(), key=lambda x: x.visits, reverse=True)[0:10]
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VideoSearchApiView(APIView):
    serializer_class = VideoSerializer

    def get(self, request, query, *args, **kwargs):
        '''
        List all the video items for given requested user
        '''
        videos = NewVideo.objects.filter(Q(title__icontains=query))
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)