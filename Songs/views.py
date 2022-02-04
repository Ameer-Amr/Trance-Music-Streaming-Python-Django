from django.shortcuts import render

from .models import Song

# Create your views here.

def song_detail(request,song_id):
    try:
        single_song = Song.objects.get(song_id=song_id)
    except Exception as e :
        raise e
    context = {
        'single_song' : single_song,

    }    
    return render(request,'user/song_detail.html',context)