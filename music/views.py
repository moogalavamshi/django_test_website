from django.http import HttpResponse
from django.shortcuts import render
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', context)


def detail_view(request, album_id):
    # html = '<h2> the album id is ' + album_id + '</h2>'
    html = ''

    return HttpResponse(html)
