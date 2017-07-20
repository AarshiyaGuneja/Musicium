
from django.shortcuts import render
from tune.models import Songs


def index(request):
    songs = Songs.objects.all()

    return render(request, 'index.html', {
        'songs': songs,
    })

def song_detail(request, slug):
    song = Songs.objects.get(slug=slug)

    return render(request, 'songs/song_detail.html', {
        'song': song,
    })

