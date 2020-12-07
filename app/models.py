from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.name
    
class Artist(models.Model):
    name = models.CharField(max_length=50)
    genres = models.CharField(max_length=100)
    listings = models.ManyToManyField(Album, related_name='artist', blank=True)

    def __str__(self):
        return self.name
    
class Song(models.Model):
    name = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    artists = models.ManyToManyField(Artist, related_name='artists', blank=True)

    def __str__(self):
        return self.name
    