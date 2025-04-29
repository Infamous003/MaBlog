from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import Http404
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    # try:
    #     post = get_object_or_404(Post, id=id)
    # except Http404:
    #     return render(request, '404.html')
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post.html', {'post': post})