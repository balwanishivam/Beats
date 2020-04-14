from django.contrib.auth.models import User
from django import forms
from .models import *


def user_directory_path_music(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/music/<filename>
    return 'user_{0}/music/{1}'.format(instance.album.id, filename)

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields=['username','password','email','first_name','last_name']

class LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','password']

class SongCreateForm(forms.ModelForm):
    class Meta:
        model=Song
        fields=['user','album','song_title','audio_file']
        exclude=('user','album',)