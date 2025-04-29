from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})