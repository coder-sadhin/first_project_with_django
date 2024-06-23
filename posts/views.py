from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import CreatePost

# Create your views here.
def posts_list(request):
    posts=Post.objects.all().order_by('-date')
    return render(request, 'posts/post_list.html',{'posts':posts})

def post_page(request, slug):
    post=Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html',{'post':post})

@login_required(login_url='users:login')
def create_post(request):
    form = CreatePost()
    return render(request, 'posts/create_post.html', {'form':form})