from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import permissions    
from video_api.models import NewVideo
from .models import comments
from .serializer import CommentSerializer
from django.http import Http404
from rest_framework.parsers import MultiPartParser

class CommentApiView(APIView):
    serializer_class = CommentSerializer
    parser_classes = (MultiPartParser, )

    # 1. List all
    def get(self,request,video_id, *args, **kwargs):
        '''
        List all the video items for given requested user
        '''
        Comments = comments.objects.get(video_id=video_id)
        serializer = CommentSerializer(Comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request,video_id, *args, **kwargs):
        '''
        Post a comment
        '''
        video = NewVideo.objects.get(pk=video_id)
        data = {
            "user": request.data.get('user'),
            "username": request.data.get('username'),
            "comment_text": request.data.get('comment_text'),
            "video": video.id
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetailApiView(APIView):
    serializer_class = CommentSerializer

    def get_comment(self, video_id, comment_id):
        try:
            return comments.objects.get(video_id=video_id, comment_id=comment_id)
        except comments.DoesNotExist:
            raise Http404
    
    '''
    # Get a video object
    # '''
    # def get(self, request, video_id,comment_id, *args, **kwargs):
    #     Comment = self.get_comment(video_id,comment_id)
    #     serializer = CommentSerializer(Comment)
    #     return Response(serializer.data)


