from django.shortcuts import render
import string
from ..models import Album

def albums(request):
    alphabets = string.ascii_uppercase
    albums = Album.objects.all()

    context = {
        'alphabets': alphabets,
        'albums': albums
    }
    return render(request, 'app/albums.html', context)