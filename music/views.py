from django.views.generic import *
from django.views.generic.edit import *
from .models import *
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(ListView):
    template_name='music/index.html'
    context_object_name='album_list'
    model=Album
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user is None:
            return qs
        return qs.filter(user=user)

class DetailView(DetailView):
    model=Album
    template_name='music/detail.html'


class AlbumCreate(LoginRequiredMixin, CreateView):
    model = Album
    fields=['artist','album_title','genre','album_logo']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AlbumUpdate(UpdateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model=Album
    success_url=reverse_lazy('music:index')

class UserFormView(View):
    form_class=UserForm
    template_name='music/registration_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('music:index')
        
        return render(request,self.template_name,{'form':form})

class LoginView(View):
    form_class=LoginForm
    template_name='music/login.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form=self.form_class(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                #messages.info(request, 'Your have successfully loged in!')
                return redirect('music:index')
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'form':form,'error_message': 'Invalid login'})
        return render(request,self.template_name,{'form':form})

class LogoutView(View):
    form_class=LoginForm
    template_name='music/login.html'
    def get(self,request):
        form=self.form_class(None)
        logout(request)
        return redirect(reverse('music:login_user'))

# class Song_Detail(DetailView):
#     model=Song
#     template_name='music/song_detail.html'


class SongCreate(View):
    form_class=SongCreateForm
    template_name='music/song_form.html'
    
    def get(self,request,pk):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request,pk):
        form=self.form_class(request.POST)
        if form.is_valid():
            song=form.save(commit=False)
            album= Album.objects.get(id=pk)
            song.album=album
            song.save()
            return redirect(reverse('music:details', kwargs={'pk': pk}))
        else:
            return render(request,self.template_name,{'form':form})



class AlbumUpdate(UpdateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model=Album
    success_url=reverse_lazy('music:index')