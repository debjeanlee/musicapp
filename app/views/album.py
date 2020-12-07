from django.shortcuts import render
from ..models import Album, Artist, Song

def album(request, id):
    album = Album.objects.get(pk=id)
    artist = Artist.objects.get(listings=id)
    songs = Song.objects.filter(album_id=id)

    context = {
        'album': album,
        'artist': artist,
        'songs': songs
    }
    return render(request, 'app/album.html', context)