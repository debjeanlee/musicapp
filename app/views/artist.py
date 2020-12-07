from django.shortcuts import render
from ..models import Artist, Song

def artist(request, id):
    artist = Artist.objects.get(pk=id)
    songs = Song.objects.filter(artists=id)

    context = {
        'artist': artist,
        'songs': songs
    }
    return render(request, 'app/artist.html', context)