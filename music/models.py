from django.db import models
  
class Album(models.Model):
    artist=models.CharField(max_length=50)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=50)
    album_logo=models.CharField(max_length=200)

    def __str__(self):
        return self.artist+'=>'+self.album_title

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=50)
    is_favourite=models.BooleanField(default=False)
    def __str__(self):
        return self.song_title+'.'+self.file_type
 


# Create your models here.
