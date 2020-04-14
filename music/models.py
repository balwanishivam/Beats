from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import os


def user_directory_path_image(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/music/<filename>
    return 'user_{0}/image/{1}'.format(instance.user.id, filename)

def user_directory_path_music(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/music/<filename>
    return 'user_{0}/music/{1}'.format(instance.user.id, filename)

class Album(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    artist=models.CharField(max_length=50)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=50)
    album_logo = models.ImageField(upload_to=user_directory_path_image, blank=True)

    def get_absolute_url(self):
        return reverse('music:details',kwargs={"pk":self.pk})

    def __str__(self):
        return self.album_title


class Song(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    album = models.ForeignKey(Album, on_delete=models.CASCADE,null=True)
    song_title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to=user_directory_path_music,blank=True)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title



# Create your models here.
