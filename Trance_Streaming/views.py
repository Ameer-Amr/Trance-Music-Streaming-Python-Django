from django.shortcuts import render
from Songs.models import Song
from django.core.paginator import Paginator

def home(request):
    songs = Song.objects.all()
    
    context = {
        'songs':songs,

    }
    return render(request, 'user/home.html', context)

def singlesong(request,song_id):
    songs = Song.objects.all()
    try:
        single_song = Song.objects.get(song_id=song_id)
    except Exception as e :
        raise e
    context = {
        'single_song' : single_song,
        'songs':songs,          


    } 
    return render(request, 'user/home.html', context)