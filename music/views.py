from django.views.generic import *
from django.views.generic.edit import *
from .models import Album


class IndexView(ListView):
    template_name='music/index.html'
    context_object_name='album_list'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(DetailView):
    model=Album
    template_name='music/detail.html'

class AlbumCreate(CreateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']

