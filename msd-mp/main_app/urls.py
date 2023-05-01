from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("logout/", views.logout, name="logout"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("trending/", views.trending, name="trending"),
    path("upload/", views.upload, name="UploadVideo"),
    path("view/<int:videoID>/", views.videoview, name="ViewVideo"),
    # re_path(r'^view/<int:videoID>/', views.videoview, name='ViewVideo')
]
