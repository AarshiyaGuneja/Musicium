
from django.shortcuts import render
from tune.models import Songs


def index(request):
    songs = Songs.objects.all()

    return render(request, 'index.html', {
        'songs': songs,
    })

