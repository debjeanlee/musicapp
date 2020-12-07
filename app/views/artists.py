from django.shortcuts import render
import string
from ..models import Artist

def artists(request):
    alphabets = string.ascii_uppercase
    artists = Artist.objects.all()

    context = {
        'alphabets': alphabets,
        'artists': artists
    }
    return render(request, 'app/artists.html', context)