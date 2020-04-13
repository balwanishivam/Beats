from django.contrib.auth.models import User
from django import forms
from .models import *

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
        fields=['album','song_title','audio_file']
        exclude=('album',)