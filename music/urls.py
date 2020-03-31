from django.urls import path

from . import views

app_name="music"

urlpatterns=[
    # /music/
    path('',views.index,name='index'),
    #/music/id/
    path('<int:album_id>/',views.details,name='details'),
    path('<int:album_id>/favourite/',views.favourite,name='favourite')
]