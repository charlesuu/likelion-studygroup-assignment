from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

def detail(request,id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'detail.html', {'post':post})

def new(request):
    return render(request,'new.html')


# Create your views here.
