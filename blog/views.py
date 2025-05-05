from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.core.exceptions import PermissionDenied
# Create your views here.

def post_list(request):
    selected_filter = request.GET.get('filter')

    if selected_filter == 'oldest':
        posts = Post.objects.order_by('created_at')
    else:
        posts = Post.objects.order_by('-created_at')

    return render(request, 'users/user_posts.html', {'posts': posts, 'selected_filter': selected_filter})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post.html', {'post': post})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        if request.user.is_authenticated:
            form = PostForm()
        else:
            return redirect('user_register')
    return render(request, 'blog/post_create.html', {'form': form})

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        if request.user.is_authenticated:
            form = PostForm(instance=post)
        else:
            raise PermissionDenied()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=id)
        post.delete()
        return redirect('post_list')
    else:
        raise PermissionDenied()

    