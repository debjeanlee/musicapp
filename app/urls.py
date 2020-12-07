from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('albums', views.albums, name='albums'),
    path('album/<int:id>', views.album, name='album'),
    path('artists', views.artists, name='artists'),
    path('artist/<int:id>', views.artist, name='artist'),
    path('songs', views.songs, name='songs'),
    path('song/<int:id>', views.song, name='song'),
]
