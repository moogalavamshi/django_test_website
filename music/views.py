from django.http import HttpResponse
from django.template import loader
from .models import Album



def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context, request))


def detail_view(request, album_id):
    # html = '<h2> the album id is ' + album_id + '</h2>'
    html = ''

    return HttpResponse(html)
