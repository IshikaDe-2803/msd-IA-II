from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields import CharField, TextField, DateField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import datetime

class NewVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    title =  models.CharField(max_length=100, default="")
    description = TextField(max_length=100, default="")
    visits= models.IntegerField(default="0")
    likes = models.IntegerField(default="0")
    dislikes = models.IntegerField(default="0")
    date = models.DateField(default=datetime.date.today)
    thumbnail = models.ImageField(upload_to='thumbnail_uploaded', default=None)
    video = models.FileField(upload_to='videos_uploaded', validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])], default=None)

    def __str__(self):
        return self.title