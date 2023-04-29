from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from video_api.models import NewVideo

class comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=1000)
    video = models.ForeignKey(NewVideo, on_delete=models.CASCADE,default=2)

    def __str__(self):
        return self.comment_text