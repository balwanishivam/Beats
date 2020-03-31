from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from .models import *
def index(request):
    all_album=Album.objects.all()
    context={
        'all_album':all_album,
    }
    return render(request,'music/index.html',context)

def details(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    return render(request,'music/detail.html',{'album':album})

def favourite(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render(request,'music/detail.html',{'album':album, 'error_message':"Not a valid song selected",})
    else:
        selected_song.is_favourite=True
        selected_song.save()
        return render(request,'music/detail.html',{'album':album})


# Create your views here.
