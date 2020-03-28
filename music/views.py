from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
def index(request):
    all_album=Album.objects.all()
    context={
        'all_album':all_album,
    }
    return render(request,'music/index.html',context)

def details(request,album_id):
    return HttpResponse("<h2>Details for album_id :"+str(album_id)+"</h2>")
# Create your views here.
