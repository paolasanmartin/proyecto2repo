from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import UserRegisterForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import User

def inicio (request):
    return render (request, 'inicio.html')

def feed(request):
    posts = Post.objects.all()

    context = {
        'posts' : posts
    }
    return render (request, 'feed.html', context)

def register(request):
    form = UserRegisterForm()
    context = {
            'form': form
        }
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        print (form.errors)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El usuario {username} fue creado')
            
            return redirect ('/feed')   
    return render (request, 'register.html', context)

def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect ('/feed')
    else:
        form = PostForm()
        context = {
            'form' : form
        }
    return render(request, 'post.html', context)
        
        

def profile(request, id=None):
    current_user = request.user
    posts = current_user.posts.all()
    context = {
        'user' : current_user,
        'posts' : posts
    }
    if id and id != current_user.id:
        user = User.objects.get(id=id)
        posts = user.posts.all()

    return render (request, 'profile.html', context)

def imagen (request):
    'form'