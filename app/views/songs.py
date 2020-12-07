from django.shortcuts import render
import string
from ..models import Song



def songs(request):
    alphabets = string.ascii_uppercase
    songs = Song.objects.all()
    context = {
        'alphabets': alphabets,
        'songs': songs
    }
    return render(request, 'app/songs.html', context)