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

# Create your views here.
