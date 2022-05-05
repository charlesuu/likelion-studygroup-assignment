from django.shortcuts import redirect, render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

def detail(request,id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'detail.html', {'post':post})

def new(request):
    return render(request,'new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.content = request.POST['contents']
    new_post.save()
    return redirect('detail', new_post.id)


def edit(request, id):
    post_for_edit = get_object_or_404(Post, pk = id)
    return render(request, 'edit.html', {'post':post_for_edit})

def update(request,id):
    update_post = get_object_or_404(Post,pk=id)
    update_post.title = request.POST['title'] 
    update_post.content = request.POST['contents']
    update_post.save()
    return redirect('detail',update_post.id)


def delete(request,id):
    delete_post = get_object_or_404(Post,pk=id)
    delete_post.delete()
    return redirect('home')
# Create your views here.
