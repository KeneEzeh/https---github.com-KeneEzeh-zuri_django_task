from email.policy import default
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=23)
    last_name = models.CharField(max_length=23)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste,on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    date_released = models.DateField()
    likes = models.IntegerField(default=0)
    artiste_id = models.IntegerField(default=0)
    

    def __str__(self) -> str:
        return self.title

class Lyric(models.Model):
    Song = models.ForeignKey(Song,on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    song_id = models.IntegerField(default=0)
    

    def __str__(self) -> str:
        return self.content
