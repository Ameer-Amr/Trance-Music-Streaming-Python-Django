from django.shortcuts import render
from Songs.models import Song
from django.core.paginator import Paginator

def home(request):
    songs = Song.objects.all()

    context = {
        'songs':songs,

    }
    return render(request, 'user/home.html', context)