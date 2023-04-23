from django.urls import path, include, re_path

from .views import (
    VideoListApiView,
)

urlpatterns = [
    path('', VideoListApiView.as_view()),
    re_path(r'^view/(?P<pk>\d+)/$', VideoListApiView.as_view()),
    
]