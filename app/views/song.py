from django.shortcuts import render
from ..models import Song

def song(request, id):
    song = Song.objects.get(pk=id)

    context = {
        'song': song
    }
    return render(request, 'app/song.html', context)