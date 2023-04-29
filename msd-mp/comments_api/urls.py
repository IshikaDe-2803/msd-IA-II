from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CommentApiView, CommentDetailApiView

urlpatterns = [
    path('videos/<int:pk>/comments/', CommentApiView.as_view()),
    path('videos/<int:video_id>/comments/<int:comment_id>/', CommentDetailApiView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)