from django.shortcuts import render
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
    try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request,'music/detail.html',{'album':album})

# Create your views here.
