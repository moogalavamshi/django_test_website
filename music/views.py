from django.http import HttpResponse
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    html = ''

    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'

    return HttpResponse(html)


def detail_view(request, album_id):
    # html = '<h2> the album id is ' + album_id + '</h2>'
    html = ''
    album = Album.objects.filter(id=album_id)
    for item in album:
        html = '<h1>' + str(item.id) + '</h1>' + '<h2>' + item.album_title + '</h2>' + '<img height = "200" src = "' + item.album_logo + '"</img>'

    return HttpResponse(html)
