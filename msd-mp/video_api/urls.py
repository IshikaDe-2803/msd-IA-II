from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import VideoListApiView, VideoDetailApiView, VideoTrendingApiView, VideoSearchApiView

urlpatterns = [
    path('', VideoListApiView.as_view()),
    path('<int:pk>', VideoDetailApiView.as_view()), 
    path('trending', VideoTrendingApiView.as_view()), 
    path('<>', VideoSearchApiView.as_view())  
]

urlpatterns = format_suffix_patterns(urlpatterns)