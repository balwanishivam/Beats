from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name="music"

urlpatterns=[
    # /music/
    path('index/',views.IndexView.as_view(),name='index'),
    path('register',views.UserFormView.as_view(),name='register'),
    path('', views.LoginView.as_view(),name='login_user'),
    path('logout_user/', views.LogoutView.as_view(),name='logout_user'),
    path('<int:pk>/',views.DetailView.as_view(),name='details'),
    # path('<int:pk>/favorite/', views.favorite, name='favorite'),
    # path('songs/<str:filter_by>/', views.songs, name='songs'),
    path('album/add/',views.AlbumCreate.as_view(),name='album_add'),
    path('album/<int:pk>/',views.AlbumUpdate.as_view(),name='album_update'),
    path('album/<int:pk>/delete',views.AlbumDelete.as_view(),name='album_delete'),
    path('album/<int:pk>/create_song/', views.SongCreate.as_view(), name='create_song'),
    path('delete_song/<int:song_id>/', views.SongDelete.as_view(), name='delete_song'),
    # path('<int:album_id>/favorite_album/', views.favorite_album, name='favorite_album'),

]
urlpatterns += staticfiles_urlpatterns()
