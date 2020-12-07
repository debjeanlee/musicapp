from django.contrib import admin
from .models import *

# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'genres')
    filter_horizontal = ('listings',)

class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'album')
    filter_horizontal = ('artists',)

admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song, SongAdmin)