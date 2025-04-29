from django.shortcuts import render, HttpResponse
from blog.views import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# def post(request):
#     return render(request, 'post.html')
